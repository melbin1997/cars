from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

print datetime.datetime.now()

###################################################################
pickle.dump({1: 2},open("variant_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XE.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5P_Titanium_AT.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_LXI.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_D.htm', 'https://www.cardekho.com/overview/BMW_1_Series/BMW_1_Series_118d_Sport_Line.htm', 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_A.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_1.0_Kappa_Magna_Plus_Optional.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Trendline.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XT.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Sportz_Celebration_Edition.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VDi.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_STD.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_T.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XZ_WO_Alloy.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Titanium_MT.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Zeta.htm', 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0_LT.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Sigma.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_S_AT_i_VTEC.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XZ_WO_Alloy.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_VXI_Optional.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_A_EPS.htm', 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.4_T-Jet_Emotion.htm', 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Dynamic.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LS.htm', 'https://www.cardekho.com/overview/Volkswagen_Beetle/Volkswagen_Beetle_1.4_TSI.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_AMT_VXI_Optional.htm', 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_E_MT.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_1.2.htm', 'https://www.cardekho.com/overview/Volkswagen_CrossPolo/Volkswagen_CrossPolo_1.2_MPI.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXE.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Comfortline.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_1.0_RXT_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_AMT_VXI.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_V.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_AT_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZDi.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_Option_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_VXI_BS_IV.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Era.htm', 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_AT.htm', 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_Up_1.2_Dynamic.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XM.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Sportz_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Magna.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XE.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XT_Option.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_LXi.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_Option_1.2.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_BS_IV.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_D.htm', 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_Petrol_RxL.htm', 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.3_Multijet_Active.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXL.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_E_i_DTEC.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Asta_Option_AT.htm', 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_Diesel_XL_Optional.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XE_Option.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VXi.htm', 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_eLX.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LTZ.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_A.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LT_ABS.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_1.0.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_AT.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_T_Option.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XM.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_AMT_VXI_Option.htm', 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Emotion.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XE.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XM_Option.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_LXI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_VXI.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXT_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LXI_Optional.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Comfortline.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XZ.htm', 'https://www.cardekho.com/overview/Fiat_Punto_Pure/Fiat_Punto_Pure_1.3L_Advanced_Multi-Jet.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XT.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LT.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZDi_Option.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LS.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XT_Option.htm', 'https://www.cardekho.com/overview/Fiat_Abarth_Avventura/Fiat_Abarth_Avventura_1.4_T-Jet.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2_S.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VDi.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_Optional.htm', 'https://www.cardekho.com/overview/Volvo_V40_Cross_Country/Volvo_V40_Cross_Country_T4.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_ZXI.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Magna_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Magna.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LS_ABS.htm', 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Sportz_1.1L.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_Green_VXI.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XT.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_CVT_Zeta.htm', 'https://www.cardekho.com/overview/Mini_5_DOOR/Mini_5_DOOR_Cooper_D.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Base_MT.htm', 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Magna_1.1L.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_T_Option.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_Optional.htm', 'https://www.cardekho.com/overview/Mini_3_DOOR/Mini_3_DOOR_Cooper_D.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_VD.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Deca.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XMS.htm', 'https://www.cardekho.com/overview/Mini_3_DOOR/Mini_3_DOOR_Cooper_S.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LDI_Optional.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_PS.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Era_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Titanium_Plus_MT.htm', 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Active.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LS.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Asta_Option.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_CVT_Delta.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XE.htm', 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_DLX_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.5L_V.htm', 'https://www.cardekho.com/overview/Volkswagen_CrossPolo/Volkswagen_CrossPolo_1.5_TDI.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_SV_i_VTEC.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XM.htm', 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_RxZ.htm', 'https://www.cardekho.com/overview/Volvo_V40/Volvo_V40_D3_R_Design.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XM_Option.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XT.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Sportz_1.2.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Era_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Fiat_Punto_Abarth/Fiat_Punto_Abarth_1.4_T-Jet.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_A_Class/Mercedes-Benz_A_Class_A200_D_Sport.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VXi_(ABS)_BS_IV.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XZ.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Asta_Option.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Era.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_AT_1.4.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_G.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LS.htm', 'https://www.cardekho.com/overview/Mahindra_e2o/Mahindra_e2o_T2.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LT.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_PS.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_Select_1.5_TDI_Highline.htm', 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Emotion.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_CNG_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_1.0_Magna_Plus_Option_O.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_GT_TSI.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4_S.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Magna_Plus_Option.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LXI.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_1.3_DLX.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.4L_VD.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_1.2.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_E_i_VTEC.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_Sport.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LDI_BSIV.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Magna_Plus.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XM.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_CNG_LXI.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XMA.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_VXI.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_VX_i_VTEC.htm', 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_XL_CVT.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_SV_i_DTEC.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VDI_Optional.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_V_AT_i_VTEC.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Sigma.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LS_ABS.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_S_i_DTEC.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XE_Option.htm', 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_VX_MT.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Deca.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_Green_VXI_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LX.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_Optional.htm', 'https://www.cardekho.com/overview/Fiat_Punto_Pure/Fiat_Punto_Pure_1.2L_FIRE.htm', 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D2.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LX_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI_Option.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LX.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_GD.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Ambiente_MT.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Zeta.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XB.htm', 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XB.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_VXI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Era_1.2.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_LDi.htm', 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_S_MT.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Era_Plus_Option.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_AT.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_CNG_LXI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Era_Plus.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.4L_GD.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_VXD.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_VX.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Titanium_MT.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Highline.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Titanium_Plus_MT.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XTA.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_AT.htm', 'https://www.cardekho.com/overview/Mini_Cooper_Countryman/Mini_Cooper_Countryman_Cooper_D.htm', 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LTZ.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_CNG.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Alpha.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi.htm', 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_RxL_Optional.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XM.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_AMT.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Highline.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Sportz.htm', 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.3_Multijet_Dynamic.htm', 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_DLS_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_AT_Optional.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XE.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_Select_1.2_MPI_Highline.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Base_MT.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_VXI_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_AMT_VXI.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_ZDi.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_A_Class/Mercedes-Benz_A_Class_A180_Sport.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4_SX_with_AVN.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_1.2_DLX.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_AT.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_ZDi.htm', 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_BS_IV.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI_Optional-O.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_AGS_Optional.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Trend_MT.htm', 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Sportz_1.1L_LPG.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_V_i_DTEC.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LT_ABS.htm', 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_Diesel_XL.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_T.htm', 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_S.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Sportz.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XT.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_CNG.htm', 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.2L_G.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_GT_1.5_TDI.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LX_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_AT_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Sportz_Celebration_Edition.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_ZXi.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Glory_Limited_Edition.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_Airbag.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite_Plus_Option.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Glory_Limited_Edition.htm', 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Era.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Delta.htm', 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_Style.htm', 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2_SX_with_AVN.htm', 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XV_S.htm', 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_CNG_XM.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Magna_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VDI_(ABS)_BS_IV.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_Std_Optional.htm', 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XMS.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Delta.htm', 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Active.htm', 'https://www.cardekho.com/overview/Volvo_V40/Volvo_V40_D3.htm', 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXT.htm', 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_VX_AT.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LDI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Sportz.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LDi.htm', 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Era_Plus_Option.htm', 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XV.htm', 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0_LS.htm', 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_eLS.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Optional.htm', 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_STD.htm', 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Dynamic.htm', 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D6.htm', 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Optional.htm', 'https://www.cardekho.com/overview/Fiat_500/Fiat_500_Abarth_595_Competizione.htm', 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI.htm', 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI.htm', 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Alpha.htm', 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Trendline.htm', 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_CNG_Optional.htm', 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D4.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_V_i_VTEC.htm', 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XL.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_S_i_VTEC.htm', 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_VX_i_DTEC.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Trend_MT.htm', 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Ambiente_MT.htm']
driver = webdriver.Chrome()
flag=0
for link in variants_dict:	
	try:
		q=time.time()
		output={}
		glink=link
		if(len(fail)>0):
			print "Couldnot obtain the details of ",len(fail)," cars"
		print ""
		print "Fetching the details of ",glink.split('/')[5].replace('_',' ').replace('.htm','')
		a=[]
		driver.get(link)

		#!!!!!print "Review"
		#!!!!!print link


		output['Review_link']=link
		

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//section[@id='variantwrap']")))

		for k in  driver.find_elements_by_xpath("//section[@id='variantwrap']"):
			#!!!!!print k.text
			a.append(k.text)


		output['Review']=a


		original = link
		s = link.split("/")
		s[3] = 'specs'
		link = '/'.join(s)
		link = link[:-4] + "-specification.htm"
		#!!!!!print "####################################################################################"
		#!!!!!print link
		

		output['Specs_link']=link


		driver.get(link)
	  #driver.switch_to.default_content()
		# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()



		############################################################################################################################

		#category = {}
		#techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//h3")
		#details = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")

		'''for count, i1 in enumerate(techf_collection):
			i1.text
		print "END"'''


		'''# Displays technical specs
		for count, i1 in enumerate(techf_collection):
			try:
				catg = i1.get_attribute('title').encode('UTF8')
				print 'catg', catg
			except Exception as e:
				pass
			#tr = techf_collection[li].find_elements_by_tag_name('tr')'''

		#IMPLICIT WAIT !!
		#driver.implicitly_wait(10)
		specs = {}


		#details_specs = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")))

		for i,j in zip(driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[@class='compareleft textalignunset']"),driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[contains(@class,'compareright')]")):
			if(j.text != '-'):
				#!!!!!!!!georgyprint i.text, '-->', j.text
				#category.setdefault(i.text.encode('UTF8')).append(j.text.encode('UTF8'))
				specs[i.text.encode('UTF8')] = j.text.encode('UTF8')
		'''if(i.get_attribute('title') != ''):
				print i.get_attribute('title')
			if(i.text != ''):
				print i.text, j.text
			'''

			#category.setdefault(catg, []).append(specs)


	############################################################################################################################

		#!!!!!print "Specifications"
		#!!!!!print specs


		output['Specs']=specs


		link = original
		s = link.split("/")
		s[3] = 'features'
		link = '/'.join(s)
		link = link[:-4] + "-features.htm"
		#!!!!!print "####################################################################################"
		#!!!!!print link


		output['Features_link']=link


		driver.get(link)


		features = {}

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")))
		#details_fe = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")
		for i,j in zip(driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[@class='compareleft textalignunset']"),driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[contains(@class,'compareright')]//div[@class='W50Percent']")):
			if('has not' not in j.get_attribute("title")):
				#!!!!!!!!georgyprint i.text, '-->', 'Yes'
				features[i.text.encode('UTF8')] = 'Yes'
				#category.setdefault(i.text.encode('UTF8')).append(j.text.encode('UTF8'))

		#!!!!!print "Features"
		#!!!!!print features


		output['Features']=features
		for i in output.keys():
			print ""
			print i
			print output[i]
		"""










						WRITE THE CODE TO TAKE THE LINK OF PHOTOS............
						THEN ADD IT AS output['photos']=[link1,link2,link3,..........,linkn]












		"""
		g[flag]=output
		pickle.dump(g,open("variant_output.p","wb"))
		flag+=1
		print ""
		print "Time taken= ",time.time()-q," seconds"
		print "Completed= ",flag,"/",len(variants_dict)
		print "Percentage completed= ",flag*100/(float(len(variants_dict)))
		print ""

	except:
		print ""
		driver.close()
		print "Coutldnot obtain the details of ",glink
		fail.append(glink)
		print "Moving to next car "
		#time.sleep(5)
		driver = webdriver.Chrome()
		flag+=1
		print ""
		print "Time taken= ",time.time()-q," seconds"
		print "Completed= ",flag,"/",len(variants_dict)
		print "Percentage completed= ",flag*100/float(len(variants_dict))
		print ""


# print
# print "Time taken = ",time.time()-q," seconds"

driver.close()
print ""
print ""
print ""
print "Failed to obtain the details of the following cars"
pickle.dump(fail,open("fail.p","wb"))
for z in fail:
	print z