from streamlit_gsheets import GSheetsConnection
import streamlit as at
from datetime import datetime
import streamlit as st
PLANS ={
    "LIMA": {
        "400 Mbps": "S/79 x 2 meses S/1.00",
        "450 Mbps": "S/89 x 2 meses S/1.00",
        "750 Mbps": "S/109 x 2 meses S/1.00",
        "750 Mbps + WINTV PREMIUM": "S/109.90 x 2 meses S/1.00",

        "850 Mbps": "S/119 x 2 meses S/1.00",
        "850 Mbps + WINTV PREMIUM": "S/119.90 x 2 meses S/1.00",
        "850 Mbps + WINTV LIGA 1 MAX PREMIUM": "S/129.90 X 2 MESES S/ 1.00",
        "1000 Mbps + MESH EN COMODATO": "S/139 x 2 meses S/1.00",
        "1000 Mbps + WINTV PREMIUM + MESH EN COMODATO": "S/139.90 x 2 meses S/1.00",
        "1000 Mbps + WINTV LIGA 1 MAX PREMIUM + MESH": "S/149.90 x 2 meses S/1.00",
        "850 Mbps + DGO HOGAR + PRIME VIDEO + LIGA 1 MAX + MESH EN COMODATO": "139.90 x 2 meses S/1.00",
    },
    "PROVINCIA": {
        "450 Mbps": "S/79 x 2 meses S/1.00",
        "550 Mbps": "S/89 x 2 meses S/1.00",
        "750 Mbps": "S/99 x 2 meses S/1.00",
        "750 Mbps + WINTV PREMIUM": "S/99.90 x 2 meses S/1.00",
        "1000 Mbps": "S/129 x 2 meses S/1.00",

        "1000 Mbps + WINTV LIGA 1 MAX PREMIUM + MESH": "S/129.90 x 2 meses S/1.00",
        "1000 Mbps + DGO HOGAR + PRIME VIDEO + LIGA 1 MAX + MESH EN COMODATO": "129.90 x 2 meses S/1.00",
 
    },
    "ADICIONAL":{
        "1 MESH (AMPLIFICADOR)": "S/9.90",
        "1 WINBOX (CONVERTIDOR)": "S/15.00",
        "2 WINBOX (CONVERTIDOR)": "S/30.00",
        "FONO WIN ( 1000 MIN. CELULARES- ILIMITADO FIJOS)  1 SOL X 6 MESES *SOLO PROVINCIA*": "S/10.00",

    }
}
CHANNELS_WINTV_PREMIUM = """
**Locales:** Nativa, Latina, América TV, Panamericana, PBO, TV Perú, Exitosa, La Tele, Global, ATV Sur, USMP TV, ATV HD, Like TV, TeleLima

**Novelas:** Azteca, Corazón, Hogar TV, Pasiones, RCN Novelas, RCN, TlNovelas

**Películas y Series:** CineClick, Cinema, Clover Channel, FMH Family, FMH Movies, Universal, Studio Universal, Sony Movies, Rewind, XTime Channel, De Película, Distrito Comedia, Golden Latino, Golden Plus

**Entretenimiento:** A&E, E!, Lifetime, USA, History, Clic TV, History 2, Telemundo, AXN, Sony Channel, Las Estrellas, Univisión, Bandamax

**Kids:** Canal IPE, Antena Uno, FMH Kids, Funbox, DreamWorks, BitMe

**Deporte:** E-sports Go, GameToon, Titan

**Noticias:** TVPE Noticias, RT, DW, France 24, RPP, VPI, NTN24, TVL

**Música:** USMP TV, Rumba TV, TOP Latino, Telehit

**Misceláneos:** Canal B, VIVA, Justicia TV, JN29, Karibeña, ASIRI, Bethel TV, BH TV, Conecta2 TV, CTV, Folklore TV, Gamarra Channel, Inka Vision HD, Milenial, NEOTV, Onda Digital, SolTV, Trivu, Visión Sur
"""

CHANNELS_LIGA1MAX = """
**Locales:** Nativa, Latina, América TV, Panamericana, PBO, TV Perú, Exitosa, La Tele, Global, ATV Sur, USMP TV, ATV HD, Like TV, TeleLima

**Novelas:** Hogar TV

**Películas:** Clover Channel

**Kids:** Canal IPE, Antena Uno

**Deporte:** Titan, L1, L1Max

**Noticias:** TVPE Noticias, RT, DW, France 24, RPP, VPI, NTN24, TVL

**Música:** USMP TV, Rumba TV, TOP Latino

**Misceláneos:** Canal B, VIVA, Justicia TV, JN29, Karibeña, ASIRI, Bethel TV, BH TV, Conecta2 TV, CTV, Folklore TV, Gamarra Channel, Inka Vision HD, Milenial, NEOTV, Onda Digital, SolTV, Trivu, Visión Sur
"""
CHANNELS_LIGA1MAX_PREMIUM = """"
**Locales:**
- Nativa
- Latina
- América TV
- Panamericana
- PBO
- TV Perú
- Exitosa
- La Tele
- Global
- ATV Sur
- USMP TV
- ATV HD
- Like TV
- TeleLima
- **Novelas**
- Azteca
- Corazón
- Hogar TV
- Pasiones
- RCN Novelas
- RCN
- TlNovelas
**Películas y Series**
- CineClick
- Cinema
- Clover Channel
- FMH Family
- FMH Movies
- Universal
- Studio Universal
- Sony Movies
- Rewind
- XTime Channel
- De Película
- Distrito Comedia
- Golden Latino
- Golden Plus
**Entretenimiento**
- A&E
- E!
- Lifetime
- USA
- History
- Clic TV
- History 2
- Telemundo
- AXN
- Sony Channel
- Las Estrellas
- Univisión
- Bandamax
**Kids**
- Canal IPE
- Antena Uno
- FMH Kids
- Funbox
- DreamWorks
- BitMe
**Deporte**
- E-sports Go
- GameToon
- Titan
- L1
- L1Max
- Noticias
- TVPE Noticias
- RT
- DW
- France 24
- RPP
- VPI
- NTN24
- TVL
**Música**
- USMP TV
- Rumba TV
- TOP Latino
- Telehit

**Misceláneos:**
- Canal B
- VIVA 
- Justicia TV
- JN29
- Karibeña
- ASIRI
- Bethel TV
- BH TV
- Conecta2 TV
- CTV
- Folklore TV
- Gamarra Channel
- Inka Vision HD
- Milenial
- NEOTV
- Onda Digital
- SolTV
- Trivu
- Visión Sur
"""
CHANNELS_DGO_HOGAR = """ 
** +30 CANALES**

**Locales:**
- Latina
- RPP
- Panamericana
- SolTV
- TVPE
- PBO
- Global
- Exitosa
- América TV
- ATV
- ATV+
- Ovación

**FreeTV (Canales FAST):**
- FreeTV TERROR
- FreeTV SABER MÁS
- FreeTV ACCIÓN
- FreeTV ESTELAR
- FreeTV DRAMA
- FreeTV HITS
- FreeTV FAMILIA
- DNews

**Deportes:**
- DSHOW
- DSports 
- DSports 2
- DSports+
- Escuela+
- L1
- L1MAX

** PAQUETE INCLUYEN:**
-  DSports 
-  Prime Video
-  L1MAX
"""


st.title("WIN - Solicita tu Plan")
zona = st.radio("¿Dónde vives?", ["LIMA", "PROVINCIA"])   
chosen_plan = st.radio("Elige tu plan:", list(PLANS[zona].keys()))
st.success(f"Precio promocional: {PLANS[zona][chosen_plan]}")

if "WINTV LIGA 1 MAX PREMIUM" in chosen_plan:
    st.info("Este plan incluye **WINTV LIGA 1 MAX PREMIUM**")
    with st.expander("Ver canaler LIGA 1 MAX "):
        st.markdown(CHANNELS_LIGA1MAX_PREMIUM)
elif "WINTV PREMIUM" in chosen_plan:
    st.info("Este plan incluye **WINTV PREMIUM**")
    with st.expander("Ver canales WINTV PREMIUM"):
        st.markdown(CHANNELS_WINTV_PREMIUM)
elif "DGO HOGAR" in chosen_plan:
    st.info("Este plan incluye **DGO HOGAR + PRIME VIDEO + LIGA 1 MAX**")
    with st.expander("Ver canales DGO HOGAR"):
        st.markdown(CHANNELS_DGO_HOGAR)
else:
    st.caption("Este plan es solo internet, sin canales de TV.")
with st.form(key='lead_form'):
    st.subheader("Tus datos para contactarte")
    name = st.text_input("Nombre Completo*" )
    dni = st.text_input("DNI / CE *")
    date_birth = st.text_input("Fecha de Nacimiento (DD/MM/AAAA) *")
    birthplace = st.text_input("Lugar de Nacimiento *")
    email = st.text_input("Correo Electrónico *")
    b_phone = st.text_input("Celular Base")
    c_phone = st.text_input("Celular Cliente *")
    district = st.text_input("Distrito *")
    address = st.text_input("Dirección exacta (calle, número) *")
    floor = st.text_input("Piso")
    apartment = st.text_input("Departamento / Interior")
    coordinates = st.text_input("Coordenadas")
    reference = st.text_input("Referencia")
    plan = st.text_input("Plan *")
    price = st.text_input("Precio Regular")

    st.subheader("Equipos adicionales (opcional)")
    mesh = st.checkbox("Mesh")
    winbox = st.checkbox("Winbox")

    st.subheader("Horario de instalación preferido")
    schedule = st.radio (
        "Elige el tramo de horario",
        [
            "Tramo 1: 8:00 a 12:00",
            "Tramo 2: 12:00 a 16:00",
            "Tramo 3: 16:00 a 20:00",
        ]
    )
    advisor = "Gustavo Medina Guzman"
    
    submitted = st.form_submit_button("Quiero contratar")
    
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/Datos/edit"
type = "service_account"
project_id = "sheet-editor-bot"
private_key_id = "106739306410969720707"
private_key = "2f5852e94c399b88e9a929e0bb22838f39c26e99"
client_email = "sheet-editor-bot@my-project-509310.iam.gserviceaccount.com"
client_id = "106739306410969720707"
auth_id = ""
token:uri = ""
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = ""

if submitted:
  if not name or not dni or not c_phone or not district or not address:
    st.error("Por favor completa los campos obligatorios marcados con *")
  else:
    conn = st.connection("gsheets", type=GSheetsConection)
    lead_data = {
      "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "Nombre": name,
      "DNI/CE": dni,
      "Celular": c_phone,
      "Distrito": district,
      "Plan": chosen_plan,
      "Horario": schedule
    }
    existing_data = conn.read(worksheet="Leads", usecols=list(range(8)),ttl=5)
    import pandas as pd
    update_df = pd_.concat([existing_data, pd.DaraFrame([lead_data])], ignore_index=True)
    conn.update(worksheet="Leads", data=update_df)
    st.balloons()
    st.success(f"Gracias {name}! Un asesor te contactará al {c_phone} en breve.")
    st.info(f"Plan: {chosen_plan} | Horario: {schedule}")
