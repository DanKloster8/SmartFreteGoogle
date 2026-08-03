---
name: Logistics Precision
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#455f88'
  primary: '#002045'
  on-primary: '#ffffff'
  primary-container: '#1a365d'
  on-primary-container: '#86a0cd'
  inverse-primary: '#adc7f7'
  secondary: '#0061a5'
  on-secondary: '#ffffff'
  secondary-container: '#66affe'
  on-secondary-container: '#004172'
  tertiary: '#002713'
  on-tertiary: '#ffffff'
  tertiary-container: '#003f23'
  on-tertiary-container: '#4bb278'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#d2e4ff'
  secondary-fixed-dim: '#9fcaff'
  on-secondary-fixed: '#001d37'
  on-secondary-fixed-variant: '#00497e'
  tertiary-fixed: '#91f8b8'
  tertiary-fixed-dim: '#74db9d'
  on-tertiary-fixed: '#002110'
  on-tertiary-fixed-variant: '#00522f'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  title-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.5'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  code-md:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  max-width: 1440px
---

## Brand & Style

The design system is engineered for high-stakes logistics management. It prioritizes **Modern Corporate** aesthetics, blending the reliability of traditional enterprise software with the efficiency of modern SaaS. The goal is to evoke a sense of absolute control, technical sophistication, and operational velocity.

The style utilizes a **Tonal Layering** approach with high-density layouts. It avoids unnecessary decoration, focusing instead on data clarity and functional hierarchy. Visual interest is generated through precise alignment, subtle color-coded status indicators, and a refined use of white space that prevents data-heavy screens from feeling overwhelming.

## Colors

The palette is anchored by **Navy Blue (#1A365D)**, representing the stability and authority required for commercial transport. **Accent Blue (#3182CE)** is used strictly for interactive elements and primary actions, signaling innovation and movement.

**Success Green (#38A169)** is reserved for conversion metrics, completed shipments, and positive growth indicators. The background utilizes a cool **Background Gray (#F7FAFC)** to reduce eye strain during long periods of data entry, while pure white (#FFFFFF) is used for "Surface" containers to create clear separation between the canvas and the content.

## Typography

This design system uses **Inter** exclusively to ensure maximum legibility across dense data tables and complex forms. 

- **Headlines:** Use tight letter spacing and heavier weights to establish clear section breaks.
- **Body Text:** Primarily uses `body-md` (14px) for the standard interface to maximize information density without compromising readability.
- **Labels:** Small, uppercase labels with increased letter spacing are used for table headers and form field descriptors to provide a structural "frame" for user data.
- **Numerical Data:** For tracking numbers or IDs, use `code-md` to ensure character clarity (e.g., distinguishing '0' from 'O').

## Layout & Spacing

The layout follows a **4px base grid** for precise alignment. A **12-column fluid grid** is used for desktop layouts, while mobile transitions to a single-column stack with 16px side margins.

- **Data Density:** Use `sm` (8px) for internal padding within components like table cells or small cards.
- **Section Grouping:** Use `lg` (24px) to separate logical groups of information.
- **Page Layout:** Containers should have a maximum width of 1440px to ensure line lengths remain readable on ultra-wide monitors common in logistics hubs.

## Elevation & Depth

This design system uses **Tonal Layering** and **Ghost Outlines** rather than heavy shadows to maintain a clean, professional look.

1.  **Level 0 (Background):** `#F7FAFC` - The base canvas.
2.  **Level 1 (Surface):** `#FFFFFF` - Used for cards and main content areas. It features a subtle 1px border of `#E2E8F0` (Neutral Gray).
3.  **Level 2 (Interactive):** When a user hovers over an item, apply a very soft, diffused shadow: `0px 4px 12px rgba(26, 54, 93, 0.05)`.
4.  **Level 3 (Overlays):** Modals and dropdowns use a slightly more pronounced shadow to indicate focus, with a backdrop blur of 4px to maintain context.

## Shapes

The design system uses a **Soft (0.25rem)** roundedness profile. This "semi-sharp" approach communicates precision and industrial robustness while feeling contemporary.

- **Standard Elements:** Buttons, input fields, and small chips use `rounded-sm` (4px).
- **Large Containers:** Data cards and dashboard panels use `rounded-lg` (8px).
- **Status Badges:** Use a higher roundedness (pill-shaped) to distinguish them from interactive buttons.

## Components

### Buttons & Inputs
- **Primary Action:** Solid `#3182CE` background with white text. High-contrast and clear.
- **Secondary Action:** Ghost style—Primary Navy border and text with transparent background.
- **Input Fields:** 1px border in `#E2E8F0`. On focus, the border shifts to Accent Blue with a 2px outer glow.

### Status Badges
Used for shipment and conversion tracking.
- **Converted:** Success Green (#38A169) background at 10% opacity with solid Green text.
- **Not Converted:** Neutral Gray background at 10% opacity with dark gray text.
- **In Transit:** Accent Blue (#3182CE) background at 10% opacity with solid Blue text.

### Data Cards & Tables
- **Cards:** White background, 1px border, 8px corner radius. Headlines inside cards should use `title-md`.
- **Tables:** Row-based hover states using `#F7FAFC`. Use "Divided" style rather than "Bordered" (lines between rows, no lines between columns).

### Interactive Charts
- Use **Primary Navy** for the main data series and **Success Green** for targets or secondary positive metrics. 
- Grid lines in charts should be extremely faint (`#EDF2F7`) to keep the focus on the data trend.
- Use `label-md` for axis titles and tooltips.