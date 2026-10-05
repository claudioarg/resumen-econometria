# -*- coding: utf-8 -*-
"""
Script para aplicar optimización móvil y responsive design 100% adaptado a teléfonos celulares
en MATRIZ_COMPARATIVA_ECONOMETRIA.html e index.html
"""

responsive_css = '''
    /* =========================================================
       DISEÑO RESPONSIVE Y OPTIMIZACIÓN MÓVIL (< 768px - CELULARES)
       ========================================================= */
    @media (max-width: 768px) {
      html, body {
        overflow-x: hidden; /* Evita que la pantalla se mueva de lado a lado */
      }
      body {
        padding: 8px 6px;
        font-size: 13.5px;
      }

      /* Header compacto para celulares */
      header {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
        margin-bottom: 10px;
        padding-bottom: 10px;
      }
      h1 {
        font-size: 1.18rem;
        flex-direction: column;
        align-items: flex-start;
        gap: 5px;
      }
      h1 span {
        font-size: 0.70rem;
        padding: 2px 7px;
      }
      p.subtitle {
        font-size: 0.80rem;
        line-height: 1.35;
      }
      header .hide-print {
        display: flex;
        justify-content: space-between;
        width: 100%;
        gap: 6px;
      }
      .theme-toggle {
        flex: 1;
        justify-content: center;
        padding: 7px 10px;
        font-size: 0.78rem;
      }
      header button.btn-action:not(.theme-toggle) {
        display: none; /* En celular no se imprime */
      }

      /* Barra de navegación pegajosa (Sticky Tabs) para cambiar de tema con un toque */
      .nav-tabs {
        position: sticky;
        top: 0;
        z-index: 100;
        background: var(--bg);
        margin-left: -6px;
        margin-right: -6px;
        padding: 8px 6px;
        gap: 6px;
        margin-bottom: 12px;
        border-bottom: 2px solid var(--accent);
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        -webkit-overflow-scrolling: touch;
      }
      .tab-btn {
        padding: 7px 12px;
        font-size: 0.80rem;
        border-radius: 6px;
        flex-shrink: 0;
        min-height: 38px;
        display: inline-flex;
        align-items: center;
      }

      /* Controles de visor de tabla en celular */
      #tab-matriz .hide-print {
        flex-direction: column;
        align-items: stretch;
        padding: 8px 10px;
        gap: 8px;
      }
      #tab-matriz .hide-print > div:last-child {
        display: flex;
        justify-content: space-between;
        width: 100%;
      }
      #tab-matriz .hide-print button {
        flex: 1;
        text-align: center;
        justify-content: center;
      }

      /* Tabla panorámica: columna congelada reducida para que el contenido se lea perfectamente */
      .panoramic-container {
        max-height: 65vh;
        border-radius: 8px;
        -webkit-overflow-scrolling: touch;
      }
      table.matrix-table {
        min-width: 1650px;
        font-size: 0.78rem;
      }
      table.matrix-table th, table.matrix-table td {
        padding: 8px 6px;
      }
      table.matrix-table th.first-col, table.matrix-table td.first-col {
        width: 100px !important;
        min-width: 100px !important;
        max-width: 100px !important;
        font-size: 0.72rem;
        padding: 6px 4px;
        word-break: break-word;
        hyphens: auto;
      }
      table.matrix-table th.first-col {
        font-size: 0.74rem;
      }
      .diff-box, .diff-plus {
        padding: 5px 6px;
        font-size: 0.72rem;
        margin-top: 4px;
      }

      /* Tarjetas de Supuestos */
      .assumption-level-card {
        padding: 12px 10px;
        margin-bottom: 12px;
        border-radius: 8px;
      }
      .level-header {
        gap: 8px;
        margin-bottom: 8px;
      }
      .level-num {
        width: 26px;
        height: 26px;
        font-size: 0.90rem;
      }
      .level-title {
        font-size: 0.98rem;
      }
      .level-tagline {
        font-size: 0.78rem;
      }
      .diagnostic-question {
        padding: 8px 10px;
        font-size: 0.82rem;
      }

      /* Ejemplos numéricos y fórmulas matemáticas */
      .full-example-card {
        padding: 12px 10px;
        border-radius: 8px;
      }
      .example-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 5px;
      }
      .example-title {
        font-size: 1.02rem;
      }
      .data-box {
        padding: 8px 10px;
        font-size: 0.80rem;
      }
      .calc-step-block {
        padding: 10px 8px;
        margin-bottom: 10px;
        border-radius: 6px;
      }
      .calc-step-title {
        font-size: 0.84rem;
      }
      .math-work {
        padding: 8px 8px;
        font-size: 0.74rem;
        line-height: 1.5;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .takeaway-box {
        padding: 8px 10px;
        font-size: 0.78rem;
      }
      .interactive-guide-banner {
        padding: 8px 10px;
        font-size: 0.78rem;
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
      }

      /* Números clickeables: toque táctil cómodo */
      .calc-num {
        padding: 2px 5px;
        font-size: 0.88em;
      }

      /* Galería Visual de Gráficos */
      .visual-gallery {
        grid-template-columns: 1fr;
        gap: 14px;
      }
      .visual-card {
        padding: 12px 10px;
        border-radius: 10px;
      }
      .svg-plot-box {
        padding: 6px;
      }
      .svg-plot-box svg {
        width: 100%;
        height: auto;
        max-height: 175px;
      }
      .visual-title {
        font-size: 0.92rem;
      }
      .visual-signature {
        padding: 6px 8px;
        font-size: 0.80rem;
      }
      .visual-details-list {
        font-size: 0.78rem;
      }
      .visual-filter-bar {
        gap: 4px;
      }
      .visual-filter-btn {
        padding: 5px 8px;
        font-size: 0.74rem;
      }
      .visual-quiz-card {
        padding: 12px 10px;
        border-radius: 10px;
      }

      /* Comparador 1 a 1 */
      .comparator-panel {
        grid-template-columns: 1fr;
        gap: 12px;
      }
      .compare-card {
        padding: 12px 10px;
      }

      /* Generador de Examen en celular */
      .exam-config-card {
        padding: 14px 10px;
        border-radius: 10px;
      }
      .exam-config-card h2 {
        font-size: 1.10rem;
      }
      .config-grid {
        grid-template-columns: 1fr;
        gap: 12px;
      }
      .config-section-title {
        font-size: 0.82rem;
      }
      .checkbox-item {
        font-size: 0.82rem;
        padding: 4px 0;
        min-height: 32px;
      }
      .exam-question-card {
        padding: 12px 10px;
        border-radius: 8px;
        margin-bottom: 12px;
      }
      .question-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
      }
      .question-text {
        font-size: 0.90rem;
        line-height: 1.4;
        margin-bottom: 10px;
      }
      .option-label {
        padding: 11px 10px;
        font-size: 0.84rem;
        gap: 8px;
        min-height: 44px; /* Tamaño táctil óptimo para el dedo */
        align-items: flex-start;
      }
      .explanation-box {
        padding: 10px 10px;
        font-size: 0.80rem;
      }
      .score-banner {
        padding: 14px 10px;
      }
      .score-number {
        font-size: 1.7rem;
      }
      #exam-bottom-actions {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
        padding: 12px 10px;
      }
      #exam-bottom-actions > div {
        display: flex;
        flex-direction: column;
        gap: 8px;
        width: 100%;
      }
      #exam-bottom-actions .btn-action {
        width: 100%;
        justify-content: center;
        padding: 12px;
        font-size: 0.92rem;
      }

      /* KaTeX fórmulas matemáticas en celular */
      .katex {
        font-size: 0.90em;
      }
      .katex-display {
        overflow-x: auto;
        overflow-y: hidden;
        -webkit-overflow-scrolling: touch;
        padding: 3px 0;
        margin: 4px 0;
      }

      /* Popover flotante convertido en Bottom Sheet moderno y deslizable en celulares */
      .num-popover {
        position: fixed !important;
        bottom: 10px !important;
        left: 8px !important;
        right: 8px !important;
        top: auto !important;
        width: auto !important;
        max-width: none !important;
        max-height: 82vh !important;
        overflow-y: auto !important;
        border-radius: 14px !important;
        box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.4) !important;
        border: 2px solid var(--accent) !important;
        padding: 14px 12px !important;
        z-index: 100000 !important;
      }
      .popover-header {
        padding-bottom: 6px;
        margin-bottom: 8px;
      }
      .popover-close {
        font-size: 1.5rem;
        padding: 4px 10px;
        min-width: 36px;
        min-height: 36px;
      }
      .popover-badge {
        font-size: 0.82rem;
        padding: 2px 6px;
      }
      .popover-origin {
        font-size: 0.82rem;
      }
      .popover-calc {
        font-size: 0.78rem;
        padding: 5px 8px;
      }
      .popover-desc {
        font-size: 0.80rem;
      }
    }
'''

with open('MATRIZ_COMPARATIVA_ECONOMETRIA.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '    /* Print Styles (100% fondo blanco, texto negro, sin tinta negra desperdiciada) */'

if target in content:
    content = content.replace(target, responsive_css + '\n' + target, 1)
    print("CSS Responsive insertado con éxito.")
else:
    print("ERROR: Target de Print Styles no encontrado.")
    exit(1)

with open('MATRIZ_COMPARATIVA_ECONOMETRIA.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("MATRIZ_COMPARATIVA_ECONOMETRIA.html e index.html actualizados.")
