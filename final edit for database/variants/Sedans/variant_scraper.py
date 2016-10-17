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
pickle.dump({1: 2},open("variant_sedan_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_sedan_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_1.6_S.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_E_Option_i-VTEC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_S_Celebration_Edition.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_i-DTEC.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_LXI_Option.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.1_CRDi_Base.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_LS_ABS.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_VL_AT.htm', 'https://www.cardekho.com/overview/Chevrolet_Cruze/Chevrolet_Cruze_LTZ.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_CVT_i-VTEC.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_2.0L_TDI_Highline_AT.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_Celeste_1.2_TSI_Highline_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_CRDi_AT_S.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_LS_(TDI)_BS-III.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VDi_Option_SHVS.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.5_TDCi_Trend.htm', 'https://www.cardekho.com/overview/Fiat_Linea/Fiat_Linea_Power_Up_1.3_Dynamic.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_2.0_TDI_MT.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_eLS_BS_IV.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_CDI_Avantgrade.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_D-4D_Limited_Edition.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_eLX_BS_IV.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.5_TDCi_Titanium.htm', 'https://www.cardekho.com/overview/Mahindra_Verito/Mahindra_Verito_1.5_Executive_edition.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.5_TDI_Highline_AT.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Revotron_1.2T_XMS.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VDI.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_RS_ZDi_Plus_SHVS.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_ZXI.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_RS_ZXi_Plus.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_VTVT_AT_SX.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLA/Mercedes-Benz_CLA_200_CDI_Style.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_i-VTEC.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_SX_VTVT.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.5_VX.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_Style_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VDi_Plus_SHVS.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.2_LS_ABS.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VXI_AT_Optional.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_eGLS_BS_IV.htm', 'https://www.cardekho.com/overview/Fiat_Linea/Fiat_Linea_Power_Up_1.3_Emotion.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_AT_Style.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.2_Ti-VCT_Titanium.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_AT_ZXi.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.2_Ti-VCT_Trend.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_CVT_SV.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_Ambition.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_Style_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_LDI.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_75PS_XM.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_XTA.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_XMA.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.2_MPI_Trendline.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.1_CRDi_S.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_D-4D_GL.htm', 'https://www.cardekho.com/overview/Audi_A3/Audi_A3_35_TDI_Premium_Plus.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_XV_CVT.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_V.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S500.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_S.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_GL_MT.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_LDI_Optional.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_VTVT_AT_S.htm', 'https://www.cardekho.com/overview/Fiat_Linea/Fiat_Linea_Power_Up_1.4_Fire_Active.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_AT_VXi_Plus.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_CRDI_SX_Option.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.4_GD.htm', 'https://www.cardekho.com/overview/Skoda_Superb/Skoda_Superb_Style_1.8_TSI_MT.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_E.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_V.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_LX_(TDI)_BS-III.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VXI_Optional.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_Momentum.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_Active.htm', 'https://www.cardekho.com/overview/Chevrolet_Cruze/Chevrolet_Cruze_LT.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.2_MPI_Comfortline.htm', 'https://www.cardekho.com/overview/Fiat_Linea_Classic/Fiat_Linea_Classic_1.3_Multijet.htm', 'https://www.cardekho.com/overview/Renault_Scala/Renault_Scala_RxL.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_AT_Style_Plus.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_2.0L_TDI_Trendline.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_KINETIC.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_AMT_ZDI.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_2.0_SX_AT.htm', 'https://www.cardekho.com/overview/Audi_A3/Audi_A3_35_TDI_Technology.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_G_AT.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.5_TDI_Highline_AT.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Style.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_E_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_1.4_TSI_Comfortline.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.4_VD.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_CRDi_SX.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_1.4_TSI_Trendline.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.5_TDI_Trendline.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_Diesel_XL.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_S.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_Diesel_XE.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.2_Base.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TDI.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_E.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_VX_i-VTEC.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.6_Highline.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_XL.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_ZXi.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VXi.htm', 'https://www.cardekho.com/overview/Mahindra_E_Verito/Mahindra_E_Verito_D2.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_SX_Option_AT.htm', 'https://www.cardekho.com/overview/Mahindra_E_Verito/Mahindra_E_Verito_D6.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_75PS_XE.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_ZXi_Plus.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_Diesel_XV.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_LT_ABS.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_Active.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_VX_CVT_i-VTEC.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Style_Plus_1.8_TSI_AT.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_ZDI.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_LXI.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_2.0_S.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S400.htm', 'https://www.cardekho.com/overview/Fiat_Linea_Classic/Fiat_Linea_Classic_Plus_1.3_Multijet.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_Option_CVT_i-VTEC.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.5_Ti-VCT_Titanium.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.1_CRDi_S_Celebration_Edition.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_2.0L_TDI_Comfortline.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_AT_Ambition.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_E_i-VTEC.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.6_Trendline.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_Edition_E.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_2.0_TDI_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_2.0_SX.htm', 'https://www.cardekho.com/overview/Ford_Mustang/Ford_Mustang_V8.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_AT_Style_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VDI_Optional.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_D-4D_JS.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Revotron_1.2T_XE.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.5_TDI_Comfortline_AT.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_VX_Option.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLA/Mercedes-Benz_CLA_200_CGI.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.5_G.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.2_TSI_Highline_AT.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VDI_SHVS.htm', 'https://www.cardekho.com/overview/Skoda_Superb/Skoda_Superb_LK_2.0_TDI_AT.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E400_Cabriolet.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_CVT_VX.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.5_V.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_VX_Option.htm', 'https://www.cardekho.com/overview/Renault_Scala/Renault_Scala_Diesel_RxZ.htm', 'https://www.cardekho.com/overview/Audi_A3/Audi_A3_35_TDI_Premium.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D5_Inscription.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.3_Base.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VXI.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_63_AMG.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_XE.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_1.6_SX.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.2_LT_ABS.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_350_CDI.htm', 'https://www.cardekho.com/overview/Mahindra_E_Verito/Mahindra_E_Verito_D4.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_XT.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_VX_Option_BL.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_Style_Plus_Black_Package.htm', 'https://www.cardekho.com/overview/Nissan_Sunny/Nissan_Sunny_XV_D_Premium_Safety.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_SX_i_VTEC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E200_Edition_E.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_AT_Style_Plus_Black_Package.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.6_MPI_Style_Plus_Black_Package.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_1.4_TSI_MT.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.1_CRDi_SX.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Style_Plus_2.0_TDI_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_VTVT_SX_Option.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Revotron_1.2T_XM.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.2_LS.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_Edition_E.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_500_Coupe.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_2.0_SX_Option.htm', 'https://www.cardekho.com/overview/Fiat_Linea/Fiat_Linea_Power_Up_1.3_Active.htm', 'https://www.cardekho.com/overview/Toyota_Camry/Toyota_Camry_2.5_G.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_Celeste_1.5_TDI_Highline.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VXi_Option.htm', 'https://www.cardekho.com/overview/Skoda_Superb/Skoda_Superb_LK_1.8_TSI_AT.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_VX_i_DTEC.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_eVX.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.5_TDI_Comfortline.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_VX.htm', 'https://www.cardekho.com/overview/Chevrolet_Sail/Chevrolet_Sail_1.3_LS.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.2_Ti-VCT_Titanium_Plus.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Revotron_1.2_XT.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_SX_Option.htm', 'https://www.cardekho.com/overview/Skoda_Superb/Skoda_Superb_Style_2.0_TDI_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.4_VTVT.htm', 'https://www.cardekho.com/overview/Audi_A3/Audi_A3_40_TFSI_Premium.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.5_TDI_Highline.htm', 'https://www.cardekho.com/overview/Mahindra_Verito/Mahindra_Verito_1.5_D2_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_ZDi_Plus_SHVS.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLA/Mercedes-Benz_CLA_45_AMG.htm', 'https://www.cardekho.com/overview/Mahindra_Verito/Mahindra_Verito_1.5_D6_BSIV.htm', 'https://www.cardekho.com/overview/Mahindra_Verito/Mahindra_Verito_1.5_D4_BSIV.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_CRDI_AT_SX_Option.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.4_CRDi.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.5_TDI_Highline.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.6_Comfortline.htm', 'https://www.cardekho.com/overview/Fiat_Linea_Classic/Fiat_Linea_Classic_1.4_Petrol.htm', 'https://www.cardekho.com/overview/Toyota_Camry/Toyota_Camry_Hybrid.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_1.6_SX_Option.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_D-4D_G.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_D-4D_J.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_VXi_Plus.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.2_MPI_Highline.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_G_MT.htm', 'https://www.cardekho.com/overview/Toyota_Etios/Toyota_Etios_1.4_VXD.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_2.0_SX_Option_AT.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.2_Ti-VCT_Ambiente.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_Plus_1.8_TSI_AT.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_63_S_AMG.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.5_TDI_Comfortline.htm', 'https://www.cardekho.com/overview/Fiat_Linea_Classic/Fiat_Linea_Classic_Plus_With_Alloy_1.3_Multijet.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_S_Option_i-VTEC.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.5_TDCi_Ambiente.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.5_TDI_Trendline.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_200_CGI.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_200_CGI.htm', 'https://www.cardekho.com/overview/Tata_Zest/Tata_Zest_Quadrajet_1.3_75PS_XMS.htm', 'https://www.cardekho.com/overview/Volkswagen_Ameo/Volkswagen_Ameo_1.5_TDI_Comfortline_AT.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_1.2_TSI_Comfortline_AT.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_Celeste_1.5_TDI_Highline_AT.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_VX.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_SX_i_DTEC.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_SV.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_T6.htm', 'https://www.cardekho.com/overview/Renault_Scala/Renault_Scala_Diesel_RxL.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_Guard.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_SX.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_VTVT_S.htm', 'https://www.cardekho.com/overview/Tata_Indigo_CS/Tata_Indigo_CS_Emax_CNG_GLS.htm', 'https://www.cardekho.com/overview/Honda_Amaze/Honda_Amaze_E_i-DTEC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Maruti_Ciaz/Maruti_Ciaz_ZDi_SHVS.htm', 'https://www.cardekho.com/overview/Hyundai_Elantra/Hyundai_Elantra_1.6_SX_Option_AT.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLA/Mercedes-Benz_CLA_200_CDI_Sport.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_S_AT.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_VXi_AT.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_Base.htm', 'https://www.cardekho.com/overview/Volkswagen_Vento/Volkswagen_Vento_Celeste_1.6_Highline.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_VTEC_VX_Option_BL.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_JS_MT.htm', 'https://www.cardekho.com/overview/Ford_Figo_Aspire/Ford_Figo_Aspire_1.5_TDCi_Titanium_Plus.htm', 'https://www.cardekho.com/overview/Chevrolet_Cruze/Chevrolet_Cruze_LTZ_AT.htm', 'https://www.cardekho.com/overview/Skoda_Superb/Skoda_Superb_Style_1.8_TSI_AT.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_Plus_2.0_TDI_MT.htm', 'https://www.cardekho.com/overview/Maruti_Swift_Dzire/Maruti_Swift_Dzire_LXI_Optional-O.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600_Guard.htm', 'https://www.cardekho.com/overview/Honda_City/Honda_City_i_DTec_SV.htm', 'https://www.cardekho.com/overview/Hyundai_Verna/Hyundai_Verna_1.6_CRDi_S.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI_Matrix.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.1_CRDi_SX_Option.htm', 'https://www.cardekho.com/overview/Hyundai_Xcent/Hyundai_Xcent_1.2_Kappa_S.htm', 'https://www.cardekho.com/overview/Toyota_Corolla_Altis/Toyota_Corolla_Altis_1.8_Limited_Edition.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG_Coupe.htm', 'https://www.cardekho.com/overview/Volkswagen_Jetta/Volkswagen_Jetta_2.0L_TDI_Highline.htm', 'https://www.cardekho.com/overview/Fiat_Linea/Fiat_Linea_125S.htm', 'https://www.cardekho.com/overview/Skoda_Octavia/Skoda_Octavia_Ambition_Plus_2.0_TDI_AT.htm', 'https://www.cardekho.com/overview/Skoda_Rapid/Skoda_Rapid_1.5_TDI_Ambition.htm']
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
		pickle.dump(g,open("variant_sedan_output.p","wb"))
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