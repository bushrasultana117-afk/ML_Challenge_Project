import streamlit as st
import requests
import pandas as pd





# PAGE CONFIGURATION



st.set_page_config(
    page_title="SentinelAI",
    page_icon="🏭",
    layout="wide"
)





# CUSTOM CSS



st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
}
.subtitle {
    font-size: 18px;
    color: #777;
}
.metric-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)





# API URL



API_URL = "http://127.0.0.1:8000"





# HEADER



st.markdown(
    '<div class="main-title">🏭 SentinelAI</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">'
    'AI-Powered Industrial Machine Health Monitoring'
    '</div>',
    unsafe_allow_html=True
)


st.divider()





# SIDEBAR



st.sidebar.title("🏭 SentinelAI")


page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "🔍 Machine Analysis"
    ]
)





# DASHBOARD



if page == "📊 Dashboard":


    st.header("📊 Machine Monitoring Dashboard")


    st.write(
        "Monitor machine health and perform AI-powered "
        "machine analysis."
    )


    
    # FASTAPI STATUS
    


    try:
        response = requests.get(
            f"{API_URL}/model-status",
            timeout=5
        )


        if response.status_code == 200:
            st.success(
                "🟢 SentinelAI AI Engine is Online"
            )
        else:
            st.warning(
                "⚠️ AI Engine is not responding correctly."
            )


    except Exception:
        st.error(
            "🔴 FastAPI backend is offline."
        )
        st.info(
            "Start FastAPI before using the dashboard."
        )


    st.divider()


    
    # OVERVIEW
 


    col1, col2, col3, col4 = st.columns(4)


    col1.metric("🏭 System", "Online")


    # Model name is longer text, not a short numeric value —
    # st.metric() clips long strings, so render it with markdown instead.
    with col2:
        st.markdown("🤖 **Model**")
        st.markdown("#### Random Forest")


    col3.metric("📡 Sensors", "5")
    col4.metric("⚡ AI Status", "Ready")


    st.divider()


   
    # SYSTEM INFORMATION
   


    st.subheader("🚀 SentinelAI System")


    st.info(
        """
        **SentinelAI** analyzes industrial machine sensor readings
        and detects abnormal machine behavior.


        The system monitors:


        🌡️ Temperature


        📳 Vibration


        💧 Humidity


        🔧 Pressure


        ⚡ Energy Consumption
        """
    )





# MACHINE ANALYSIS



elif page == "🔍 Machine Analysis":


    st.header("🔍 Machine Analysis")


    st.write(
        "Enter machine information and sensor readings."
    )


   
    # MACHINE INFORMATION
   


    st.subheader("🏭 Machine Information")


    factory_name = st.text_input(
        "Factory Name",
        placeholder="e.g. ABC Manufacturing"
    )


    machine_id = st.text_input(
        "Machine ID",
        placeholder="e.g. CNC-001"
    )


   
    # SENSOR INPUTS
    


    st.subheader("📊 Sensor Readings")


    temperature = st.number_input(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=0.1
    )


    vibration = st.number_input(
        "📳 Vibration",
        min_value=0.0,
        max_value=100.0,
        value=0.3,
        step=0.01
    )


    humidity = st.number_input(
        "💧 Humidity",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=0.1
    )


    pressure = st.number_input(
        "🔧 Pressure",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=0.1
    )


    energy_consumption = st.number_input(
        "⚡ Energy Consumption",
        min_value=0.0,
        max_value=10000.0,
        value=120.0,
        step=0.1
    )


    st.divider()


   
    # ANALYZE MACHINE
   


    if st.button(
        "🔍 Analyze Machine",
        use_container_width=True
    ):


       
        # VALIDATION
     


        if not factory_name.strip():
            st.warning("⚠️ Please enter the Factory Name.")
            st.stop()


        if not machine_id.strip():
            st.warning("⚠️ Please enter the Machine ID.")
            st.stop()


       
        # REQUEST DATA
       


        payload = {
            "factory_name": factory_name,
            "machine_id": machine_id,
            "temperature": temperature,
            "vibration": vibration,
            "humidity": humidity,
            "pressure": pressure,
            "energy_consumption": energy_consumption
        }


        
        # API REQUEST
        


        with st.spinner("🤖 Analyzing machine sensor data..."):
            try:
                response = requests.post(
                    f"{API_URL}/predict",
                    json=payload,
                    timeout=10
                )
            except requests.exceptions.ConnectionError:
                st.error("🔴 Cannot connect to FastAPI.")
                st.stop()


       
        # API RESPONSE
       


        if response.status_code != 200:
            st.error("❌ Prediction failed.")
            st.code(response.text)
            st.stop()


        result = response.json()


        prediction = result["prediction"]
        confidence = result["confidence"]
        health_score = result["health_score"]
        risk_level = result["risk_level"]
        recommendations = result["recommendations"]


       
        # RESULT
      


        st.divider()
        st.header("🤖 Analysis Result")


        
        # STATUS
        


        if prediction == "ANOMALY":
            st.error("🚨 ANOMALY DETECTED")
        else:
            st.success("✅ MACHINE IS NORMAL")


        
        # MACHINE DETAILS
       


        st.write(f"**Factory:** {factory_name}")
        st.write(f"**Machine ID:** {machine_id}")


       
        # METRICS
       


        col1, col2, col3 = st.columns(3)


        col1.metric(
            "🤖 Confidence",
            f"{confidence * 100:.2f}%" if confidence is not None else "N/A"
        )


        col2.metric("❤️ Health Score", f"{health_score}/100")


        col3.metric("⚠️ Risk Level", risk_level)


        st.divider()


       
        # SENSOR SUMMARY
       


        st.subheader("📊 Sensor Summary")


        sensor_data = pd.DataFrame({
            "Sensor": [
                "Temperature",
                "Vibration",
                "Humidity",
                "Pressure",
                "Energy Consumption"
            ],
            "Value": [
                temperature,
                vibration,
                humidity,
                pressure,
                energy_consumption
            ]
        })


        st.dataframe(
            sensor_data,
            use_container_width=True,
            hide_index=True
        )


       
        # RECOMMENDATIONS
       

        st.subheader("🔧 Recommended Actions")


        for recommendation in recommendations:
            st.warning(recommendation)


        if prediction == "ANOMALY":
            st.info(
                "⚠️ Please inspect the machine "
                "before continuing normal operation."
            )
        else:
            st.info(
                "✅ No abnormal behavior was "
                "detected from the provided readings."
            )





# FOOTER



st.divider()


st.caption(
    "SentinelAI • AI-Powered Industrial "
    "Machine Monitoring System"
)

