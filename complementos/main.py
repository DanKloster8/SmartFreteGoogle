from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io

app = FastAPI(title="Smartfrete API de Cálculo")

# Permitir requisições de qualquer origem (ou você pode colocar o link exato da sua Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "online", "sistema": "Smartfrete Motor de Cálculo API"}

@app.post("/api/calcular")
async def api_calcular(
    origem: str = Form(...),
    destino: str = Form(...),
    distancia_km: float = Form(...),
    peso_carga: float = Form(...),
    simulacoes_hoje: int = Form(1),
    file: UploadFile = File(...)
):
    # Regra de Limite do Plano Free (3 simulações)
    LIMITE_DIARIO = 3
    if simulacoes_hoje > LIMITE_DIARIO:
        return {
            "status": "bloqueado",
            "mensagem": "Limite diário de 3 simulações gratuitas atingido. Faça upgrade para o Plano Standard!"
        }
    
    try:
        contents = await file.read()
        df_tarifas = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar o arquivo de tarifas: {str(e)}")
    
    # Varredura da faixa de peso na tabela do cliente
    tarifa_aplicada = 0.0
    faixa_encontrada = "Padrão"
    
    for index, row in df_tarifas.iterrows():
        faixa_str = str(row['Faixa_Peso_kg'])
        if '-' in faixa_str:
            limite_inf, limite_sup = map(int, faixa_str.split('-'))
            if limite_inf <= peso_carga <= limite_sup:
                tarifa_aplicada = float(row['Valor_Por_KM'])
                faixa_encontrada = faixa_str
                break
        elif '+' in faixa_str:
            limite_inf = int(faixa_str.replace('+', ''))
            if peso_carga >= limite_inf:
                tarifa_aplicada = float(row['Valor_Por_KM'])
                faixa_encontrada = faixa_str
                break

    if tarifa_aplicada == 0.0 and not df_tarifas.empty:
        tarifa_aplicada = float(df_tarifas.iloc[0]['Valor_Por_KM'])
        faixa_encontrada = "Padrão (Fallback)"

    # Cálculo final
    valor_total_frete = distancia_km * tarifa_aplicada

    return {
        "status": "sucesso",
        "origem": origem,
        "destino": destino,
        "distancia_km": distancia_km,
        "peso_carga_kg": peso_carga,
        "faixa_peso": faixa_encontrada,
        "tarifa_por_km": tarifa_aplicada,
        "valor_total_frete": round(valor_total_frete, 2),
        "limite_restante": LIMITE_DIARIO - simulacoes_hoje
    }