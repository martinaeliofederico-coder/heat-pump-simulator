import streamlit as st
import streamlit.components.v1 as components
from CoolProp.CoolProp import PropsSI


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heat Pump Simulator",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# AUXILIARY FUNCTIONS
# ============================================================

def mostrar_html(codigo):
    st.html(codigo)


def generar_svg_bomba_calor(
    T_fuente_entrada_C,
    T_fuente_salida_C,
    Q_evap_disponible_kW,
    nombre_visible_ref,
    T_evap_C,
    T_cond_C,
    COP_electrico,
    P_electrica_kW,
    Q_cond_total_kW,
    m_ref,
    T_sink_entrada_C,
    T_sink_salida_C,
    m_agua_sink_kg_h
):

    return f"""
    <!DOCTYPE html>

    <html>

    <head>

        <style>

            body {{
                margin: 0;
                padding: 0;
                background: transparent;
                font-family: Arial, sans-serif;
            }}

            .diagram-container {{
                width: 100%;
                background: white;
                border: 1px solid #e1e7ed;
                border-radius: 18px;
                padding: 15px;
                box-sizing: border-box;
                box-shadow: 0 3px 12px rgba(0,0,0,0.05);
            }}

        </style>

    </head>

    <body>

    <div class="diagram-container">

    <svg
        viewBox="0 0 1200 500"
        width="100%"
        height="480"
        xmlns="http://www.w3.org/2000/svg"
    >

        <defs>

            <linearGradient
                id="pumpGrad"
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
            >
                <stop
                    offset="0%"
                    stop-color="#143b5d"
                />

                <stop
                    offset="100%"
                    stop-color="#2389a8"
                />
            </linearGradient>


            <linearGradient
                id="sourceGrad"
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
            >
                <stop
                    offset="0%"
                    stop-color="#e5f3fa"
                />

                <stop
                    offset="100%"
                    stop-color="#cce7f5"
                />
            </linearGradient>


            <linearGradient
                id="sinkGrad"
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
            >
                <stop
                    offset="0%"
                    stop-color="#fff3d6"
                />

                <stop
                    offset="100%"
                    stop-color="#ffd985"
                />
            </linearGradient>


            <filter
                id="shadow"
                x="-20%"
                y="-20%"
                width="140%"
                height="140%"
            >
                <feDropShadow
                    dx="0"
                    dy="4"
                    stdDeviation="6"
                    flood-opacity="0.15"
                />
            </filter>


            <marker
                id="arrowBlue"
                markerWidth="12"
                markerHeight="12"
                refX="10"
                refY="6"
                orient="auto"
            >
                <path
                    d="M0,0 L12,6 L0,12 z"
                    fill="#2b6cb0"
                />
            </marker>


            <marker
                id="arrowOrange"
                markerWidth="12"
                markerHeight="12"
                refX="10"
                refY="6"
                orient="auto"
            >
                <path
                    d="M0,0 L12,6 L0,12 z"
                    fill="#d97706"
                />
            </marker>


            <marker
                id="arrowGreen"
                markerWidth="12"
                markerHeight="12"
                refX="10"
                refY="6"
                orient="auto"
            >
                <path
                    d="M0,0 L12,6 L0,12 z"
                    fill="#23815d"
                />
            </marker>

        </defs>


        <!-- TITLE -->

        <text
            x="600"
            y="38"
            text-anchor="middle"
            font-family="Arial"
            font-size="25"
            font-weight="700"
            fill="#17324d"
        >
            HEAT PUMP
        </text>


        <text
            x="600"
            y="64"
            text-anchor="middle"
            font-family="Arial"
            font-size="13"
            fill="#718096"
        >
            Industrial Heat Recovery System
        </text>


        <!-- HEAT SOURCE -->

        <rect
            x="35"
            y="180"
            rx="22"
            ry="22"
            width="230"
            height="145"
            fill="url(#sourceGrad)"
            stroke="#4a90b8"
            stroke-width="2.5"
            filter="url(#shadow)"
        />


        <text
            x="150"
            y="213"
            text-anchor="middle"
            font-family="Arial"
            font-size="19"
            font-weight="700"
            fill="#17324d"
        >
            HEAT SOURCE
        </text>


        <text
            x="150"
            y="246"
            text-anchor="middle"
            font-family="Arial"
            font-size="15"
            fill="#17324d"
        >
            {T_fuente_entrada_C:.1f} → {T_fuente_salida_C:.1f} °C
        </text>


        <text
            x="150"
            y="278"
            text-anchor="middle"
            font-family="Arial"
            font-size="18"
            font-weight="700"
            fill="#2b6cb0"
        >
            {Q_evap_disponible_kW:,.0f} kW
        </text>


        <text
            x="150"
            y="302"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            fill="#64778a"
        >
            Heat recovered
        </text>


        <!-- EVAPORATOR ARROW -->

        <line
            x1="265"
            y1="252"
            x2="400"
            y2="252"
            stroke="#2b6cb0"
            stroke-width="6"
            marker-end="url(#arrowBlue)"
        />


        <text
            x="330"
            y="228"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            font-weight="700"
            fill="#2b6cb0"
        >
            EVAPORATOR
        </text>


        <!-- HEAT PUMP -->

        <rect
            x="405"
            y="105"
            rx="30"
            ry="30"
            width="390"
            height="290"
            fill="url(#pumpGrad)"
            stroke="#102d46"
            stroke-width="3"
            filter="url(#shadow)"
        />


        <text
            x="600"
            y="145"
            text-anchor="middle"
            font-family="Arial"
            font-size="28"
            font-weight="700"
            fill="white"
        >
            HEAT PUMP
        </text>


        <text
            x="600"
            y="174"
            text-anchor="middle"
            font-family="Arial"
            font-size="17"
            font-weight="700"
            fill="#d9f3ff"
        >
            {nombre_visible_ref}
        </text>


        <!-- EVAPORATION -->

        <rect
            x="438"
            y="202"
            rx="12"
            ry="12"
            width="145"
            height="62"
            fill="#ffffff"
            fill-opacity="0.15"
            stroke="#ffffff"
            stroke-opacity="0.65"
        />


        <text
            x="510"
            y="224"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            font-weight="700"
            fill="white"
        >
            EVAPORATION
        </text>


        <text
            x="510"
            y="249"
            text-anchor="middle"
            font-family="Arial"
            font-size="18"
            font-weight="700"
            fill="white"
        >
            {T_evap_C:.1f} °C
        </text>


        <!-- CONDENSATION -->

        <rect
            x="617"
            y="202"
            rx="12"
            ry="12"
            width="145"
            height="62"
            fill="#ffffff"
            fill-opacity="0.15"
            stroke="#ffffff"
            stroke-opacity="0.65"
        />


        <text
            x="689"
            y="224"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            font-weight="700"
            fill="white"
        >
            CONDENSATION
        </text>


        <text
            x="689"
            y="249"
            text-anchor="middle"
            font-family="Arial"
            font-size="18"
            font-weight="700"
            fill="white"
        >
            {T_cond_C:.1f} °C
        </text>


        <!-- COP -->

        <rect
            x="438"
            y="284"
            rx="12"
            ry="12"
            width="145"
            height="67"
            fill="#ffffff"
            fill-opacity="0.15"
            stroke="#ffffff"
            stroke-opacity="0.65"
        />


        <text
            x="510"
            y="306"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            font-weight="700"
            fill="white"
        >
            ELECTRIC COP
        </text>


        <text
            x="510"
            y="335"
            text-anchor="middle"
            font-family="Arial"
            font-size="23"
            font-weight="700"
            fill="white"
        >
            {COP_electrico:.2f}
        </text>


        <!-- REFRIGERANT FLOW -->

        <rect
            x="617"
            y="284"
            rx="12"
            ry="12"
            width="145"
            height="67"
            fill="#ffffff"
            fill-opacity="0.15"
            stroke="#ffffff"
            stroke-opacity="0.65"
        />


        <text
            x="689"
            y="306"
            text-anchor="middle"
            font-family="Arial"
            font-size="11"
            font-weight="700"
            fill="white"
        >
            REFRIGERANT FLOW
        </text>


        <text
            x="689"
            y="335"
            text-anchor="middle"
            font-family="Arial"
            font-size="19"
            font-weight="700"
            fill="white"
        >
            {m_ref:.2f} kg/s
        </text>


        <!-- CONDENSER ARROW -->

        <line
            x1="795"
            y1="252"
            x2="930"
            y2="252"
            stroke="#d97706"
            stroke-width="6"
            marker-end="url(#arrowOrange)"
        />


        <text
            x="862"
            y="228"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            font-weight="700"
            fill="#d97706"
        >
            CONDENSER
        </text>


        <!-- HOT WATER -->

        <rect
            x="935"
            y="180"
            rx="22"
            ry="22"
            width="230"
            height="145"
            fill="url(#sinkGrad)"
            stroke="#d3a32b"
            stroke-width="2.5"
            filter="url(#shadow)"
        />


        <text
            x="1050"
            y="213"
            text-anchor="middle"
            font-family="Arial"
            font-size="19"
            font-weight="700"
            fill="#17324d"
        >
            HOT WATER
        </text>


        <text
            x="1050"
            y="242"
            text-anchor="middle"
            font-family="Arial"
            font-size="15"
            fill="#17324d"
        >
            {T_sink_entrada_C:.1f} → {T_sink_salida_C:.1f} °C
        </text>


        <text
            x="1050"
            y="272"
            text-anchor="middle"
            font-family="Arial"
            font-size="18"
            font-weight="700"
            fill="#c46b09"
        >
            {Q_cond_total_kW:,.0f} kW
        </text>


        <text
            x="1050"
            y="299"
            text-anchor="middle"
            font-family="Arial"
            font-size="12"
            fill="#64778a"
        >
            Water flow: {m_agua_sink_kg_h:,.0f} kg/h
        </text>


        <!-- ELECTRICAL POWER -->

        <line
            x1="600"
            y1="454"
            x2="600"
            y2="397"
            stroke="#23815d"
            stroke-width="6"
            marker-end="url(#arrowGreen)"
        />


        <rect
            x="480"
            y="442"
            rx="14"
            ry="14"
            width="240"
            height="43"
            fill="#e3f4eb"
            stroke="#23815d"
            stroke-width="2"
        />


        <text
            x="600"
            y="469"
            text-anchor="middle"
            font-family="Arial"
            font-size="15"
            font-weight="700"
            fill="#1d684b"
        >
            ELECTRIC POWER: {P_electrica_kW:,.0f} kW
        </text>

    </svg>

    </div>

    </body>

    </html>
    """


# ============================================================
# MAIN CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f4f7fb;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: rgba(0,0,0,0);
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    .hero {
        background: linear-gradient(
            135deg,
            #0f2740 0%,
            #164d6d 55%,
            #207a8a 100%
        );

        padding: 30px 35px;
        border-radius: 18px;
        margin-bottom: 20px;

        box-shadow:
            0 8px 24px
            rgba(15,39,64,0.16);
    }

    .hero-title {
        color: white;
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        color: #d9edf5;
        font-size: 16px;
        margin-bottom: 0px;
    }

    .hero-badge {
        display: inline-block;
        background-color: rgba(255,255,255,0.15);
        color: white;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
        margin-top: 15px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #17324d;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .section-subtitle {
        color: #6c7a89;
        font-size: 13px;
        margin-top: -2px;
        margin-bottom: 15px;
    }

    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 14px;

        box-shadow:
            0 3px 12px
            rgba(0,0,0,0.06);

        border:
            1px solid
            #e4e9ef;

        min-height: 120px;
    }

    .metric-title {
        color: #697888;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #17324d;
        font-size: 28px;
        font-weight: 700;
    }

    .metric-unit {
        color: #8593a0;
        font-size: 12px;
        margin-top: 3px;
    }

    .heat-card {
        border-top: 5px solid #e67e22;
    }

    .electric-card {
        border-top: 5px solid #3498db;
    }

    .tpe-card {
        border-top: 5px solid #27ae60;
    }

    .saving-card {
        border-top: 5px solid #16a085;
    }

    .cost-card {
        border-top: 5px solid #c0392b;
    }

    .payback-card {
        border-top: 5px solid #8e44ad;
    }

    section[data-testid="stSidebar"] {
        background-color: #eef3f7;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

mostrar_html(
    """
    <div class="hero">

        <div class="hero-title">
            Heat Pump Simulator
        </div>

        <div class="hero-subtitle">
            Industrial Heat Recovery • High Temperature Heat Pump
            • Flash Steam • Thermocompressor
        </div>

        <div class="hero-badge">
            ENERGY & FLUIDS • PRE-STUDY TOOL
        </div>

    </div>
    """
)


# ============================================================
# REFRIGERANTS
# ============================================================

MAPA_REFRIGERANTES = {

    "R1233zd(E)":
        "R1233zd(E)",

    "R134a":
        "R134a",

    "R717 (Ammonia)":
        "Ammonia",
}


REFRIGERANTES_BLOQUEADOS = {

    "R450A":
        "R450A is not enabled in this version of the simulator. "
        "The current CoolProp HEOS installation shows numerical "
        "instability for this refrigerant blend. "
        "REFPROP integration is recommended for a robust R450A evaluation."
}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## ⚙️ Simulation Inputs"
    )

    st.caption(
        "Define the process conditions and press Calculate."
    )

    st.divider()


    # ========================================================
    # HEAT SOURCE
    # ========================================================

    with st.expander(
        "🔥 Heat Source",
        expanded=True
    ):

        Q_evap_disponible_kW = st.number_input(
            "Available heat",
            min_value=0.0,
            value=450.0,
            step=10.0,
            help="Recoverable heat available at the evaporator."
        )

        st.caption(
            "kW"
        )


        T_fuente_entrada_C = st.number_input(
            "Heat source inlet temperature",
            value=80.0,
            step=1.0
        )

        st.caption(
            "°C"
        )


        T_fuente_salida_C = st.number_input(
            "Heat source outlet temperature",
            value=35.0,
            step=1.0
        )

        st.caption(
            "°C"
        )


    # ========================================================
    # HEAT PUMP
    # ========================================================

    with st.expander(
        "♨️ Heat Pump",
        expanded=True
    ):

        nombre_visible_ref = st.selectbox(
            "Refrigerant",
            [
                "R1233zd(E)",
                "R134a",
                "R450A",
                "R717 (Ammonia)"
            ]
        )


        approach_evap_C = st.number_input(
            "Evaporator approach",
            value=5.0,
            step=0.5
        )

        st.caption(
            "°C"
        )


        approach_cond_C = st.number_input(
            "Condenser approach",
            value=5.0,
            step=0.5
        )

        st.caption(
            "°C"
        )


        eta_isentropica = (
            st.number_input(
                "Compressor isentropic efficiency",
                min_value=1.0,
                max_value=100.0,
                value=75.0,
                step=1.0
            )
            / 100
        )

        st.caption(
            "%"
        )


        eta_motor = (
            st.number_input(
                "Motor efficiency",
                min_value=1.0,
                max_value=100.0,
                value=95.0,
                step=1.0
            )
            / 100
        )

        st.caption(
            "%"
        )


    # ========================================================
    # HOT WATER
    # ========================================================

    with st.expander(
        "💧 Hot Water",
        expanded=True
    ):

        T_sink_entrada_C = st.number_input(
            "Water inlet temperature",
            value=105.0,
            step=1.0
        )

        st.caption(
            "°C"
        )


        T_sink_salida_C = st.number_input(
            "Water outlet temperature",
            value=120.0,
            step=1.0
        )

        st.caption(
            "°C"
        )


    # ========================================================
    # FLASH & THERMOCOMPRESSOR
    # ========================================================

    with st.expander(
        "💨 Flash & Thermocompressor"
    ):

        P_flash_bar_abs = st.number_input(
            "Flash pressure",
            min_value=0.1,
            value=1.5,
            step=0.1
        )

        st.caption(
            "bar abs"
        )


        P_motriz_bar_g = st.number_input(
            "Motive steam pressure",
            min_value=0.0,
            value=14.0,
            step=0.5
        )

        st.caption(
            "bar(g)"
        )


        P_descarga_bar_g = st.number_input(
            "Discharge pressure",
            min_value=0.0,
            value=8.0,
            step=0.5
        )

        st.caption(
            "bar(g)"
        )


        ER = st.number_input(
            "Entrainment Ratio",
            min_value=0.01,
            value=0.30,
            step=0.01,
            format="%.2f"
        )


    # ========================================================
    # ECONOMICS & KPI
    # ========================================================

    with st.expander(
        "💰 Economics & KPI",
        expanded=True
    ):

        costo_electricidad_usd_kwh = st.number_input(
            "Electricity cost",
            min_value=0.0,
            value=0.10,
            step=0.01,
            format="%.4f"
        )

        st.caption(
            "USD/kWh"
        )


        costo_combustible_usd_mj = st.number_input(
            "Fuel cost",
            min_value=0.0,
            value=0.010,
            step=0.001,
            format="%.5f"
        )

        st.caption(
            "USD/MJ"
        )


        eta_caldera = (
            st.number_input(
                "Boiler efficiency",
                min_value=1.0,
                max_value=100.0,
                value=90.0,
                step=1.0
            )
            / 100
        )

        st.caption(
            "%"
        )


        horas_operacion_anual = st.number_input(
            "Annual operating hours",
            min_value=1.0,
            value=8000.0,
            step=100.0
        )

        st.caption(
            "h/year"
        )


        volumen_anual_hl = st.number_input(
            "Annual production",
            min_value=1.0,
            value=10000000.0,
            step=100000.0,
            format="%.0f"
        )

        st.caption(
            "hl/year"
        )


        inversion_usd = st.number_input(
            "CAPEX",
            min_value=0.0,
            value=1000000.0,
            step=100000.0,
            format="%.0f"
        )

        st.caption(
            "USD"
        )


    st.divider()


    calcular = st.button(
        "🚀 CALCULATE",
        type="primary",
        use_container_width=True
    )


# ============================================================
# INITIAL STATE
# ============================================================

if not calcular:

    mostrar_html(
        """
        <div style="
            background:white;
            border:1px solid #e1e7ed;
            border-radius:16px;
            padding:35px;
            text-align:center;
            margin-top:20px;
        ">

            <div style="
                font-size:28px;
                font-weight:700;
                color:#17324d;
            ">
                Ready to simulate
            </div>

            <div style="
                margin-top:8px;
                color:#718096;
                font-size:15px;
            ">
                Configure the process conditions in the left panel
                and press CALCULATE.
            </div>

        </div>
        """
    )


# ============================================================
# CALCULATION
# ============================================================

if calcular:

    try:

        # ====================================================
        # REFRIGERANT
        # ====================================================

        if nombre_visible_ref in REFRIGERANTES_BLOQUEADOS:

            st.error(
                "⚠️ "
                +
                REFRIGERANTES_BLOQUEADOS[
                    nombre_visible_ref
                ]
            )

            st.stop()


        refrigerante_local = (
            MAPA_REFRIGERANTES[
                nombre_visible_ref
            ]
        )


        # ====================================================
        # VALIDATIONS
        # ====================================================

        if Q_evap_disponible_kW <= 0:

            raise ValueError(
                "Available heat must be greater than zero."
            )


        if (
            T_fuente_entrada_C
            <=
            T_fuente_salida_C
        ):

            raise ValueError(
                "Heat source inlet temperature must be higher "
                "than the heat source outlet temperature."
            )


        if (
            T_sink_salida_C
            <=
            T_sink_entrada_C
        ):

            raise ValueError(
                "Hot water outlet temperature must be higher "
                "than the inlet temperature."
            )


        if ER <= 0:

            raise ValueError(
                "The Entrainment Ratio must be greater than zero."
            )


        # ====================================================
        # CYCLE TEMPERATURES
        # ====================================================

        T_evap_C = (
            T_fuente_salida_C
            -
            approach_evap_C
        )


        T_cond_C = (
            T_sink_salida_C
            +
            approach_cond_C
        )


        T_evap_K = (
            T_evap_C
            +
            273.15
        )


        T_cond_K = (
            T_cond_C
            +
            273.15
        )


        # ====================================================
        # CRITICAL TEMPERATURE
        # ====================================================

        T_crit_K = PropsSI(
            "Tcrit",
            refrigerante_local
        )


        T_crit_C = (
            T_crit_K
            -
            273.15
        )


        margen_critico_C = (
            T_crit_C
            -
            T_cond_C
        )


        if (
            T_cond_C
            >=
            T_crit_C
        ):

            raise ValueError(
                f"{nombre_visible_ref}: "
                f"Condensing temperature = {T_cond_C:.1f} °C "
                f"is above the critical temperature "
                f"({T_crit_C:.1f} °C)."
            )


        # ====================================================
        # REFRIGERATION CYCLE
        # ====================================================

        P_evap = PropsSI(
            "P",
            "T", T_evap_K,
            "Q", 1,
            refrigerante_local
        )


        P_cond = PropsSI(
            "P",
            "T", T_cond_K,
            "Q", 0,
            refrigerante_local
        )


        h1 = PropsSI(
            "H",
            "T", T_evap_K,
            "Q", 1,
            refrigerante_local
        )


        s1 = PropsSI(
            "S",
            "T", T_evap_K,
            "Q", 1,
            refrigerante_local
        )


        h2s = PropsSI(
            "H",
            "P", P_cond,
            "S", s1,
            refrigerante_local
        )


        h2 = (
            h1
            +
            (
                h2s
                -
                h1
            )
            /
            eta_isentropica
        )


        T2 = PropsSI(
            "T",
            "P", P_cond,
            "H", h2,
            refrigerante_local
        )


        h3 = PropsSI(
            "H",
            "T", T_cond_K,
            "Q", 0,
            refrigerante_local
        )


        h4 = h3


        T4 = PropsSI(
            "T",
            "P", P_evap,
            "H", h4,
            refrigerante_local
        )


        Q4 = PropsSI(
            "Q",
            "P", P_evap,
            "H", h4,
            refrigerante_local
        )


        # ====================================================
        # HEAT PUMP ENERGY BALANCE
        # ====================================================

        w_comp = (
            h2
            -
            h1
        )


        q_evap = (
            h1
            -
            h4
        )


        q_cond = (
            h2
            -
            h3
        )


        if q_evap <= 0:

            raise ValueError(
                "Evaporator specific heat transfer "
                "is less than or equal to zero."
            )


        if w_comp <= 0:

            raise ValueError(
                "Compressor specific work "
                "is less than or equal to zero."
            )


        m_ref = (
            Q_evap_disponible_kW
            /
            (
                q_evap
                /
                1000
            )
        )


        P_comp_eje_kW = (
            m_ref
            *
            w_comp
            /
            1000
        )


        P_electrica_kW = (
            P_comp_eje_kW
            /
            eta_motor
        )


        Q_cond_total_kW = (
            m_ref
            *
            q_cond
            /
            1000
        )


        COP_electrico = (
            Q_cond_total_kW
            /
            P_electrica_kW
        )


        # ====================================================
        # HOT WATER
        # ====================================================

        P_sink_Pa = (
            3.0
            *
            100000
        )


        h_sink_in = PropsSI(
            "H",
            "T",
            T_sink_entrada_C + 273.15,
            "P",
            P_sink_Pa,
            "Water"
        )


        h_sink_out = PropsSI(
            "H",
            "T",
            T_sink_salida_C + 273.15,
            "P",
            P_sink_Pa,
            "Water"
        )


        delta_h_sink = (
            h_sink_out
            -
            h_sink_in
        )


        if delta_h_sink <= 0:

            raise ValueError(
                "The hot water enthalpy difference "
                "is less than or equal to zero."
            )


        m_agua_sink = (
            Q_cond_total_kW
            /
            (
                delta_h_sink
                /
                1000
            )
        )


        m_agua_sink_kg_h = (
            m_agua_sink
            *
            3600
        )


        # ====================================================
        # FLASH
        # ====================================================

        P_flash_Pa = (
            P_flash_bar_abs
            *
            100000
        )


        T_flash_C = (
            PropsSI(
                "T",
                "P", P_flash_Pa,
                "Q", 0,
                "Water"
            )
            -
            273.15
        )


        h_flash_liquido = PropsSI(
            "H",
            "P", P_flash_Pa,
            "Q", 0,
            "Water"
        )


        h_flash_vapor = PropsSI(
            "H",
            "P", P_flash_Pa,
            "Q", 1,
            "Water"
        )


        x_flash = (
            (
                h_sink_out
                -
                h_flash_liquido
            )
            /
            (
                h_flash_vapor
                -
                h_flash_liquido
            )
        )


        x_flash = max(
            0,
            min(
                1,
                x_flash
            )
        )


        m_vapor_flash_kg_h = (
            m_agua_sink
            *
            x_flash
            *
            3600
        )


        # ====================================================
        # THERMOCOMPRESSOR
        # ====================================================

        m_motriz_TC = (
            m_vapor_flash_kg_h
            /
            ER
        )


        m_salida_TC = (
            m_vapor_flash_kg_h
            +
            m_motriz_TC
        )


        # ====================================================
        # ANNUAL ENERGY
        # ====================================================

        energia_termica_util_anual_MJ = (
            Q_cond_total_kW
            *
            horas_operacion_anual
            *
            3.6
        )


        combustible_evitado_anual_MJ = (
            energia_termica_util_anual_MJ
            /
            eta_caldera
        )


        energia_electrica_anual_kWh = (
            P_electrica_kW
            *
            horas_operacion_anual
        )


        energia_electrica_anual_MJ = (
            energia_electrica_anual_kWh
            *
            3.6
        )


        # ====================================================
        # ENERGY KPI
        # ====================================================

        heat_kpi_reduction = (
            combustible_evitado_anual_MJ
            /
            volumen_anual_hl
        )


        ee_kpi_increase = (
            energia_electrica_anual_MJ
            /
            volumen_anual_hl
        )


        tpe_kpi_reduction = (
            heat_kpi_reduction
            -
            ee_kpi_increase
        )


        # ====================================================
        # ECONOMICS
        # ====================================================

        fuel_cost_avoided = (
            combustible_evitado_anual_MJ
            *
            costo_combustible_usd_mj
        )


        electricity_cost = (
            energia_electrica_anual_kWh
            *
            costo_electricidad_usd_kwh
        )


        net_annual_saving = (
            fuel_cost_avoided
            -
            electricity_cost
        )


        if net_annual_saving > 0:

            payback_years = (
                inversion_usd
                /
                net_annual_saving
            )

        else:

            payback_years = None


        # ====================================================
        # SUCCESS STATUS
        # ====================================================

        st.success(
            "✓ Simulation completed successfully"
        )


        # ====================================================
        # MAIN RESULTS
        # ====================================================

        mostrar_html(
            """
            <div class="section-title">
                Main Results
            </div>

            <div class="section-subtitle">
                Performance of the selected heat pump configuration
            </div>
            """
        )


        c1, c2, c3, c4 = st.columns(4)


        with c1:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        ELECTRIC COP
                    </div>

                    <div class="metric-value">
                        {COP_electrico:.2f}
                    </div>

                    <div class="metric-unit">
                        Qcond / Pel
                    </div>

                </div>
                """
            )


        with c2:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        ELECTRIC POWER
                    </div>

                    <div class="metric-value">
                        {P_electrica_kW:,.0f}
                    </div>

                    <div class="metric-unit">
                        kW
                    </div>

                </div>
                """
            )


        with c3:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        CONDENSER HEAT
                    </div>

                    <div class="metric-value">
                        {Q_cond_total_kW:,.0f}
                    </div>

                    <div class="metric-unit">
                        kW
                    </div>

                </div>
                """
            )


        with c4:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        REFRIGERANT FLOW
                    </div>

                    <div class="metric-value">
                        {m_ref:.2f}
                    </div>

                    <div class="metric-unit">
                        kg/s
                    </div>

                </div>
                """
            )


        st.write("")


        c5, c6, c7, c8 = st.columns(4)


        with c5:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        WATER FLOW
                    </div>

                    <div class="metric-value">
                        {m_agua_sink_kg_h:,.0f}
                    </div>

                    <div class="metric-unit">
                        kg/h
                    </div>

                </div>
                """
            )


        with c6:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        FLASH STEAM
                    </div>

                    <div class="metric-value">
                        {m_vapor_flash_kg_h:,.0f}
                    </div>

                    <div class="metric-unit">
                        kg/h
                    </div>

                </div>
                """
            )


        with c7:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        MOTIVE STEAM
                    </div>

                    <div class="metric-value">
                        {m_motriz_TC:,.0f}
                    </div>

                    <div class="metric-unit">
                        kg/h
                    </div>

                </div>
                """
            )


        with c8:

            mostrar_html(
                f"""
                <div class="metric-card">

                    <div class="metric-title">
                        DISCHARGE STEAM
                    </div>

                    <div class="metric-value">
                        {m_salida_TC:,.0f}
                    </div>

                    <div class="metric-unit">
                        kg/h
                    </div>

                </div>
                """
            )


        # ====================================================
        # HEAT PUMP VISUAL DIAGRAM
        # ====================================================

        mostrar_html(
            """
            <div class="section-title">
                Heat Pump Visual Diagram
            </div>

            <div class="section-subtitle">
                Simplified dynamic schematic with the main operating values
            </div>
            """
        )


        svg_bomba = generar_svg_bomba_calor(

            T_fuente_entrada_C=
                T_fuente_entrada_C,

            T_fuente_salida_C=
                T_fuente_salida_C,

            Q_evap_disponible_kW=
                Q_evap_disponible_kW,

            nombre_visible_ref=
                nombre_visible_ref,

            T_evap_C=
                T_evap_C,

            T_cond_C=
                T_cond_C,

            COP_electrico=
                COP_electrico,

            P_electrica_kW=
                P_electrica_kW,

            Q_cond_total_kW=
                Q_cond_total_kW,

            m_ref=
                m_ref,

            T_sink_entrada_C=
                T_sink_entrada_C,

            T_sink_salida_C=
                T_sink_salida_C,

            m_agua_sink_kg_h=
                m_agua_sink_kg_h
        )


        components.html(
            svg_bomba,
            height=540,
            scrolling=False
        )


        # ====================================================
        # ENERGY KPI
        # ====================================================

        mostrar_html(
            """
            <div class="section-title">
                Energy KPI Impact
            </div>
            """
        )


        k1, k2, k3 = st.columns(3)


        with k1:

            mostrar_html(
                f"""
                <div class="metric-card heat-card">

                    <div class="metric-title">
                        HEAT KPI REDUCTION
                    </div>

                    <div class="metric-value">
                        {heat_kpi_reduction:.3f}
                    </div>

                    <div class="metric-unit">
                        MJ/hl
                    </div>

                </div>
                """
            )


        with k2:

            mostrar_html(
                f"""
                <div class="metric-card electric-card">

                    <div class="metric-title">
                        ELECTRICITY KPI INCREASE
                    </div>

                    <div class="metric-value">
                        +{ee_kpi_increase:.3f}
                    </div>

                    <div class="metric-unit">
                        MJ/hl
                    </div>

                </div>
                """
            )


        with k3:

            mostrar_html(
                f"""
                <div class="metric-card tpe-card">

                    <div class="metric-title">
                        TPE KPI REDUCTION
                    </div>

                    <div class="metric-value">
                        {tpe_kpi_reduction:.3f}
                    </div>

                    <div class="metric-unit">
                        MJ/hl
                    </div>

                </div>
                """
            )


        # ====================================================
        # BUSINESS CASE
        # ====================================================

        mostrar_html(
            """
            <div class="section-title">
                Business Case
            </div>
            """
        )


        b1, b2, b3, b4 = st.columns(4)


        with b1:

            mostrar_html(
                f"""
                <div class="metric-card saving-card">

                    <div class="metric-title">
                        FUEL COST AVOIDED
                    </div>

                    <div class="metric-value">
                        ${fuel_cost_avoided:,.0f}
                    </div>

                    <div class="metric-unit">
                        USD/year
                    </div>

                </div>
                """
            )


        with b2:

            mostrar_html(
                f"""
                <div class="metric-card cost-card">

                    <div class="metric-title">
                        ELECTRICITY COST
                    </div>

                    <div class="metric-value">
                        ${electricity_cost:,.0f}
                    </div>

                    <div class="metric-unit">
                        USD/year
                    </div>

                </div>
                """
            )


        with b3:

            mostrar_html(
                f"""
                <div class="metric-card saving-card">

                    <div class="metric-title">
                        NET ANNUAL SAVING
                    </div>

                    <div class="metric-value">
                        ${net_annual_saving:,.0f}
                    </div>

                    <div class="metric-unit">
                        USD/year
                    </div>

                </div>
                """
            )


        with b4:

            if payback_years is not None:

                payback_text = (
                    f"{payback_years:.2f}"
                )

                payback_unit = (
                    "years"
                )

            else:

                payback_text = (
                    "N/A"
                )

                payback_unit = (
                    "No positive saving"
                )


            mostrar_html(
                f"""
                <div class="metric-card payback-card">

                    <div class="metric-title">
                        SIMPLE PAYBACK
                    </div>

                    <div class="metric-value">
                        {payback_text}
                    </div>

                    <div class="metric-unit">
                        {payback_unit}
                    </div>

                </div>
                """
            )


        # ====================================================
        # ANNUAL ENERGY BALANCE
        # ====================================================

        with st.expander(
            "📊 Annual Energy Balance"
        ):

            e1, e2, e3 = st.columns(3)


            e1.metric(
                "Useful Heat Recovered",
                f"{energia_termica_util_anual_MJ / 1000:,.0f} GJ/year"
            )


            e2.metric(
                "Purchased Fuel Avoided",
                f"{combustible_evitado_anual_MJ / 1000:,.0f} GJ/year"
            )


            e3.metric(
                "Electricity Consumption",
                f"{energia_electrica_anual_kWh / 1000:,.0f} MWh/year"
            )


        # ====================================================
        # THERMODYNAMIC CYCLE DETAILS
        # ====================================================

        with st.expander(
            "🔬 Thermodynamic Cycle Details"
        ):

            d1, d2, d3, d4 = st.columns(4)


            with d1:

                st.markdown(
                    "#### Point 1"
                )

                st.write(
                    "Compressor suction"
                )

                st.write(
                    f"**Temperature:** {T_evap_C:.2f} °C"
                )

                st.write(
                    f"**Pressure:** "
                    f"{P_evap / 100000:.2f} bar abs"
                )

                st.write(
                    f"**Enthalpy:** "
                    f"{h1 / 1000:.2f} kJ/kg"
                )


            with d2:

                st.markdown(
                    "#### Point 2"
                )

                st.write(
                    "Compressor discharge"
                )

                st.write(
                    f"**Temperature:** "
                    f"{T2 - 273.15:.2f} °C"
                )

                st.write(
                    f"**Pressure:** "
                    f"{P_cond / 100000:.2f} bar abs"
                )

                st.write(
                    f"**Enthalpy:** "
                    f"{h2 / 1000:.2f} kJ/kg"
                )


            with d3:

                st.markdown(
                    "#### Point 3"
                )

                st.write(
                    "Condenser outlet"
                )

                st.write(
                    f"**Temperature:** "
                    f"{T_cond_C:.2f} °C"
                )

                st.write(
                    f"**Pressure:** "
                    f"{P_cond / 100000:.2f} bar abs"
                )

                st.write(
                    f"**Enthalpy:** "
                    f"{h3 / 1000:.2f} kJ/kg"
                )


            with d4:

                st.markdown(
                    "#### Point 4"
                )

                st.write(
                    "Expansion valve outlet"
                )

                st.write(
                    f"**Temperature:** "
                    f"{T4 - 273.15:.2f} °C"
                )

                st.write(
                    f"**Pressure:** "
                    f"{P_evap / 100000:.2f} bar abs"
                )

                st.write(
                    f"**Enthalpy:** "
                    f"{h4 / 1000:.2f} kJ/kg"
                )

                st.write(
                    f"**Vapor quality:** "
                    f"{Q4:.3f}"
                )


        # ====================================================
        # REFRIGERANT STATUS
        # ====================================================

        st.info(
            f"**{nombre_visible_ref}**  |  "
            f"Critical temperature: {T_crit_C:.2f} °C  |  "
            f"Condensing temperature: {T_cond_C:.2f} °C  |  "
            f"Critical margin: {margen_critico_C:.2f} °C"
        )


        if margen_critico_C < 10:

            st.warning(
                "⚠️ The refrigerant is operating less than "
                "10 °C below its critical temperature. "
                "This condition should be carefully reviewed "
                "before actual equipment selection."
            )


    except Exception as error:

        st.error(
            f"❌ Calculation error: {error}"
        )