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
pickle.dump({1: 2},open("variant_suv_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_suv_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N6_AMT.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GL-Class/Mercedes-Benz_GL-Class_350_CDI_Blue_Efficiency.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X6_M.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T4_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_Thar/Mahindra_Thar_CRDe.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W10_FWD.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Evoque/Land_Rover_Range_Rover_Evoque_Pure.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_Seats_BSIII.htm', 'https://www.cardekho.com/overview/BMW_X6/BMW_X6_xDrive_40d_M_Sport.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T8_AMT.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_110PS_Diesel_RxZ_AMT.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Sport/Land_Rover_Range_Rover_Sport_S.htm', 'https://www.cardekho.com/overview/Volvo_XC60/Volvo_XC60_D4_Momentum.htm', 'https://www.cardekho.com/overview/BMW_X1/BMW_X1_xDrive_20d_xLine.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_VTVT_Anniversary_Edition.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K4_Plus_5str.htm', 'https://www.cardekho.com/overview/Toyota_Land_Cruiser/Toyota_Land_Cruiser_VX.htm', 'https://www.cardekho.com/overview/Maruti_Gypsy/Maruti_Gypsy_King_Hard_Top_MPI_BSIV.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_D5_Inscription.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_VDi_Option.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K8_5str.htm', 'https://www.cardekho.com/overview/Mahindra_Quanto/Mahindra_Quanto_C4.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Trend_Plus.htm', 'https://www.cardekho.com/overview/Porsche_Macan/Porsche_Macan_Turbo.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_200_Delta.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_S_Diesel.htm', 'https://www.cardekho.com/overview/Force_Gurkha/Force_Gurkha_Soft_Top_BS3_2WD.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W6_2WD.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S6_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W6_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N8_AMT.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W10_AWD.htm', 'https://www.cardekho.com/overview/BMW_X5/BMW_X5_xDrive_30d_Expedition.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K6.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W8_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-VTEC_V_CVT.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_mHAWK100_T8_AMT.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_CRDi4_DX.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.4_CRDi_S_Plus.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_GX.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Getaway.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_4x4_MT.htm', 'https://www.cardekho.com/overview/BMW_X5/BMW_X5_xDrive_30d_Design_Pure_Experience_7_Seater.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_S_Hybrid.htm', 'https://www.cardekho.com/overview/Tata_New_Safari/Tata_New_Safari_DICOR_2.2_EX_4x2_BS_IV.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.4_CRDi_Base.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_Non_AC_BSIV_PS.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_85PS_Diesel_STD.htm', 'https://www.cardekho.com/overview/Audi_Q3/Audi_Q3_35_TDI_Quattro_Premium.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Special_Edition.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_Gamma_SX_Plus.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_TD4_HSE_7S.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S6_Plus.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_VTVT_AT_SX_Plus.htm', 'https://www.cardekho.com/overview/Ford_Endeavour/Ford_Endeavour_3.2_Titanium_AT_4X4.htm', 'https://www.cardekho.com/overview/Mahindra_Quanto/Mahindra_Quanto_C8.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Evoque/Land_Rover_Range_Rover_Evoque_Coupe_HSE_Dynamic.htm', 'https://www.cardekho.com/overview/Skoda_Yeti/Skoda_Yeti_Style_4X2.htm', 'https://www.cardekho.com/overview/Mahindra_Quanto/Mahindra_Quanto_C6.htm', 'https://www.cardekho.com/overview/Skoda_Yeti/Skoda_Yeti_Style_4X4.htm', 'https://www.cardekho.com/overview/Mahindra_Quanto/Mahindra_Quanto_C2.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_4.4_SDV8_Autobiography_Black_Edition.htm', 'https://www.cardekho.com/overview/Maruti_Gypsy/Maruti_Gypsy_King_Hard_Top_Ambulance_BSIV.htm', 'https://www.cardekho.com/overview/BMW_X1/BMW_X1_xDrive_20d_M_Sport.htm', 'https://www.cardekho.com/overview/Hyundai_Santa_Fe/Hyundai_Santa_Fe_4WD_AT.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_mHAWK_D70_SLE.htm', 'https://www.cardekho.com/overview/Force_One/Force_One_SX_ABS_6_Seating.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_EX_BSIII.htm', 'https://www.cardekho.com/overview/Chevrolet_Trailblazer/Chevrolet_Trailblazer_LTZ_4X2_AT.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_mHAWK_D70_SLX.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W8_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_110PS_Diesel_RxL_AMT.htm', 'https://www.cardekho.com/overview/Force_One/Force_One_4x4.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S4.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S8.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Sport/Land_Rover_Range_Rover_Sport_Autobiography.htm', 'https://www.cardekho.com/overview/Audi_Q5/Audi_Q5_30_TDI_quattro_Technology.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GL-Class/Mercedes-Benz_GL-Class_63_AMG.htm', 'https://www.cardekho.com/overview/Conquest_Evade/Conquest_Evade_SUV.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K6_Plus.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_T8_Excellence.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_DI_NON_AC_BS_III_White.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_S10_AT_2WD.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K6_5str.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_110PS_Diesel_RxZ_AWD.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_D5_Momentum.htm', 'https://www.cardekho.com/overview/Tata_New_Safari/Tata_New_Safari_DICOR_2.2_LX_4x2_BS_IV.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W6_2WD.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W4.htm', 'https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N4_Plus.htm', 'https://www.cardekho.com/overview/Nissan_Terrano/Nissan_Terrano_XL.htm', 'https://www.cardekho.com/overview/Ford_Endeavour/Ford_Endeavour_3.2_Trend_AT_4X4.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X5_M.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_SD4_HSE_Luxury_7S.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_AT_S_Plus.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-VTEC_VX_MT.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.0_Ecoboost_Titanium_Plus_BE.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M6_Gran_Coupe.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_5.0_V8_Autobiography_Black_Edition.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_320_Delta.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S10.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T6.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T4.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T8.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_4x2_Manual.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_Petrol_GX.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_Base.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_SLX_2WD_BSIII.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLA/Mercedes-Benz_GLA_45_AMG.htm', 'https://www.cardekho.com/overview/Ford_Endeavour/Ford_Endeavour_2.2_Trend_MT_4X4.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Titanium_Plus_BE.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Evoque/Land_Rover_Range_Rover_Evoque_HSE.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T6_Plus.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.0_Ecoboost_Trend_Plus_BE.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_200_Alpha.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-VTEC_E_MT.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W10_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_MT_Titanium_BE.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_CRDi4_LX.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_ZDi.htm', 'https://www.cardekho.com/overview/Isuzu_MU_7/Isuzu_MU_7_AT_Premium.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_TD4_SE.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_CX_BSIII.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Evoque/Land_Rover_Range_Rover_Evoque_HSE_Dynamic.htm', 'https://www.cardekho.com/overview/Honda_CR-V/Honda_CR-V_2.0L_2WD_AT.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_4/Land_Rover_Discovery_4_SDV6_SE.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_TD4_SE_7S.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_ZLX_BSIII.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_AT_SX_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K4_Plus.htm', 'https://www.cardekho.com/overview/Jeep_Grand_Cherokee/Jeep_Grand_Cherokee_Summit_4X4.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_S2_7_Seater.htm', 'https://www.cardekho.com/overview/Ford_Endeavour/Ford_Endeavour_2.2_Titanium_AT_4X2.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Titanium.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-DTEC_V_MT.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_LX_4WD_NON_AC_BSIV.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_VTVT_E.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_3.0_Vogue.htm', 'https://www.cardekho.com/overview/BMW_X1/BMW_X1_sDrive_20d_xLine.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_VTVT_S.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_EX.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_ZLX.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.0_Ecoboost_Titanium_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K2_Plus.htm', 'https://www.cardekho.com/overview/Porsche_Macan/Porsche_Macan_2L.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLA_Class/Mercedes-Benz_GLA_Class_200.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K4_5str.htm', 'https://www.cardekho.com/overview/Mahindra_Ssangyong_Rexton/Mahindra_Ssangyong_Rexton_RX6.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M3_Sedan.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_85PS_Diesel_RxE.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M5_Sedan.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_DX_Beige_Interior.htm', 'https://www.cardekho.com/overview/Honda_CR-V/Honda_CR-V_2.4L_4WD_AT.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K8_5str.htm', 'https://www.cardekho.com/overview/Toyota_Land_Cruiser_Prado/Toyota_Land_Cruiser_Prado_VX_L.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K6_5str.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W8_FWD.htm', 'https://www.cardekho.com/overview/Mahindra_Thar/Mahindra_Thar_DI_4X4.htm', 'https://www.cardekho.com/overview/Mahindra_Thar/Mahindra_Thar_DI_4X2.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_AT_Titanium_BE.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K6_Plus_5str.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-DTEC_VX_MT.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_Petrol_RxE.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Trend_Plus_BE.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_Petrol_RxL.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_LX_4WD_NON_AC_BS3.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_CX_PS_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_-_Non-AC_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_320_Zeta.htm', 'https://www.cardekho.com/overview/Nissan_Terrano/Nissan_Terrano_XV_D_Premium_AMT.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K4_5str.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_mHAWK100_T8_Dual_Tone.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K8.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_TD4_S.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K4.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K2.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W8_2WD.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLE_Class/Mercedes-Benz_GLE_Class_350d.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_EX_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_-_AC_BSIII.htm', 'https://www.cardekho.com/overview/Force_One/Force_One_SX_ABS_7_Seating.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_DI_-_AC_BS_III.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_mHAWK_D70_ZLX.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLA_Class/Mercedes-Benz_GLA_Class_200_CDI_SPORT.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_Non_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_S8_7C_Seater.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_MT_Ambiente.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLS/Mercedes-Benz_GLS_350d_4MATIC.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_C_BSIII.htm', 'https://www.cardekho.com/overview/Volvo_XC60/Volvo_XC60_D4_KINETIC.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_320_Alpha.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S4_Plus_4WD.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_AC_BSIV_PS.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_TD4_HSE.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_LX_NON_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_AC.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_VTVT_E_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLA_Class/Mercedes-Benz_GLA_Class_200_CDI.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLC_Class/Mercedes-Benz_GLC_Class_220d_4MATIC_Style.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_LDi_Option.htm', 'https://www.cardekho.com/overview/Volvo_XC60/Volvo_XC60_D5_Inscription.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_GX_Beieg_Interior.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLC_Class/Mercedes-Benz_GLC_Class_220d_4MATIC_Sport.htm', 'https://www.cardekho.com/overview/BMW_X5/BMW_X5_xDrive_30d_Design_Pure_Experience_5_Seater.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_Adventure_Edition_RXZ_AWD.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_2.5_4x2_MT_TRD_Sportivo.htm', 'https://www.cardekho.com/overview/Maruti_Gypsy/Maruti_Gypsy_King_Soft_Top_MPI_BSIV.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_MT_Trend.htm', 'https://www.cardekho.com/overview/Audi_Q7/Audi_Q7_45_TDI_Quattro_Technology.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_ZDi_Plus.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_VDi.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M4_Coupe.htm', 'https://www.cardekho.com/overview/Jeep_Wrangler/Jeep_Wrangler_4X4.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K2_Plus.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_Anniversary_Edition.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_T6_Plus_AMT.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Ambiente.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_AT_Signature.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Titanium_Plus.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_CX_PS.htm', 'https://www.cardekho.com/overview/Jeep_Grand_Cherokee/Jeep_Grand_Cherokee_SRT_4X4.htm', 'https://www.cardekho.com/overview/Audi_Q5/Audi_Q5_45_TDI_quattro_Technology.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_AC_BSIII_PS.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_SX_Plus.htm', 'https://www.cardekho.com/overview/Mitsubishi_Pajero/Mitsubishi_Pajero_Sport_4X2_AT.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_4.4_SDV8_Vogue_SE.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_Turbo.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-VTEC_S_MT.htm', 'https://www.cardekho.com/overview/BMW_X1/BMW_X1_sDrive20d_Expedition.htm', 'https://www.cardekho.com/overview/Audi_Q5/Audi_Q5_30_TDI_quattro_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_LX_NON_AC_BS3.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K4_Plus.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_GTS.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W10_2WD.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_4.4_SDV8_Autobiography.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_Petrol_GLX.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_EX_NON_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Getaway_4WD.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K8.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_4x2_AT.htm', 'https://www.cardekho.com/overview/Honda_CR-V/Honda_CR-V_2.0L_2WD_MT.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K2.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K6.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K4.htm', 'https://www.cardekho.com/overview/Mitsubishi_Pajero/Mitsubishi_Pajero_Sport_4X2_AT_Dual_Tone.htm', 'https://www.cardekho.com/overview/Mahindra_Thar/Mahindra_Thar_DI_4X2_PS.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Sport/Land_Rover_Range_Rover_Sport_SE.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_LDi.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLE_Class/Mercedes-Benz_GLE_Class_400_4MATIC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLE_Class/Mercedes-Benz_GLE_Class_Coupe.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover/Land_Rover_Range_Rover_LWB_5.0_V8.htm', 'https://www.cardekho.com/overview/BMW_X3/BMW_X3_xDrive20d_xLine.htm', 'https://www.cardekho.com/overview/Audi_Q7/Audi_Q7_45_TDI_Quattro_Premium_Plus.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_200_Zeta.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S10_4WD.htm', 'https://www.cardekho.com/overview/Audi_Q3/Audi_Q3_30_TDI_S_Edition.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.4_CRDi_S.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_Plus_-_Non-AC_BSIII_PS.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_DX.htm', 'https://www.cardekho.com/overview/Mitsubishi_Pajero/Mitsubishi_Pajero_Sport_4X4.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Sport/Land_Rover_Range_Rover_Sport_HSE.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_Diesel.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_SX_Option.htm', 'https://www.cardekho.com/overview/BMW_X3/BMW_X3_xDrive30d_M_Sport.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Trend.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_Turbo_S.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLC_Class/Mercedes-Benz_GLC_Class_300_4MATIC_Sport.htm', 'https://www.cardekho.com/overview/Mahindra_TUV_300/Mahindra_TUV_300_mHAWK100_T8.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-VTEC_V_MT.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_2.5_4x2_AT_TRD_Sportivo.htm', 'https://www.cardekho.com/overview/Maruti_Vitara_Brezza/Maruti_Vitara_Brezza_ZDi_Plus_Dual_Tone.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_S10_AT_4WD.htm', 'https://www.cardekho.com/overview/Audi_Q3/Audi_Q3_35_TDI_Dynamic_Edition.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S4_Plus_4WD.htm', 'https://www.cardekho.com/overview/Bentley_Bentayga/Bentley_Bentayga_6.0_W12.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S10_4WD.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Sport/Land_Rover_Range_Rover_Sport_SVR.htm', 'https://www.cardekho.com/overview/BMW_X3/BMW_X3_xDrive20d_Expedition.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-DTEC_E_MT.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_SLX.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_G_Class/Mercedes-Benz_G_Class_G63_AMG.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_SLE.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_4/Land_Rover_Discovery_4_SDV6_HSE.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_M-Class/Mercedes-Benz_M-Class_ML_63_AMG_4MATIC.htm', 'https://www.cardekho.com/overview/Nissan_Terrano/Nissan_Terrano_XL_Plus_85_PS.htm', 'https://www.cardekho.com/overview/Hyundai_Santa_Fe/Hyundai_Santa_Fe_2WD_MT.htm', 'https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N4.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_MT_Signature.htm', 'https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N6.htm', 'https://www.cardekho.com/overview/Mahindra_NuvoSport/Mahindra_NuvoSport_N8.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_MT_Titanium.htm', 'https://www.cardekho.com/overview/Porsche_Cayenne/Porsche_Cayenne_S.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S10.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S4_Plus.htm', 'https://www.cardekho.com/overview/Porsche_Macan/Porsche_Macan_S_Diesel.htm', 'https://www.cardekho.com/overview/Tata_Safari_Storme/Tata_Safari_Storme_VX_4WD_Varicor_400.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.0_Ecoboost_Trend_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W10_AWD.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_110PS_Diesel_RxL.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LT_9_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S8.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_110PS_Diesel_RxZ.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Intelli_Hybrid_S4.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_85PS_Diesel_RxZ.htm', 'https://www.cardekho.com/overview/Tata_Safari_Storme/Tata_Safari_Storme_VX_Varicor_400.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_DI_NON_AC_BS_III_SILVER.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K6_Plus_5str.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Adventure_Edition_2WD.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_85PS_Diesel_RxL.htm', 'https://www.cardekho.com/overview/Mahindra_Ssangyong_Rexton/Mahindra_Ssangyong_Rexton_RX5.htm', 'https://www.cardekho.com/overview/Toyota_Fortuner/Toyota_Fortuner_4x4_AT.htm', 'https://www.cardekho.com/overview/Mahindra_Ssangyong_Rexton/Mahindra_Ssangyong_Rexton_RX7.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLS/Mercedes-Benz_GLS_400_4MATIC.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_Si4_HSE.htm', 'https://www.cardekho.com/overview/Force_Gurkha/Force_Gurkha_Hard_Top_BS3_4WD.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_Adventure_Edition_4WD.htm', 'https://www.cardekho.com/overview/BMW_X5/BMW_X5_xDrive_30d_M_Sport.htm', 'https://www.cardekho.com/overview/Nissan_Terrano/Nissan_Terrano_XV_Premium_110_PS.htm', 'https://www.cardekho.com/overview/Land_Rover_Range_Rover_Evoque/Land_Rover_Range_Rover_Evoque_SE.htm', 'https://www.cardekho.com/overview/Hyundai_Creta/Hyundai_Creta_1.6_CRDi_SX.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_Adventure_Edition_85PS_RXE.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_D75_K4_Plus_5str.htm', 'https://www.cardekho.com/overview/Force_One/Force_One_EX.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W4_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Renault_Duster/Renault_Duster_Adventure_Edition_85PS_RXL.htm', 'https://www.cardekho.com/overview/Land_Rover_Discovery_Sport/Land_Rover_Discovery_Sport_SD4_HSE_Luxury.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_Ti_VCT_AT_Titanium.htm', 'https://www.cardekho.com/overview/Mahindra_Scorpio/Mahindra_Scorpio_1.99_S4_Plus.htm', 'https://www.cardekho.com/overview/Audi_Q3/Audi_Q3_35_TDI_Quattro_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_KUV_100/Mahindra_KUV_100_mFALCON_G80_K6_Plus.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W8_4WD.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_W6_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Mahindra_XUV500/Mahindra_XUV500_AT_W10_1.99_mHawk.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Signature.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_GLE_Class/Mercedes-Benz_GLE_Class_250d.htm', 'https://www.cardekho.com/overview/Tata_Safari_Storme/Tata_Safari_Storme_EX.htm', 'https://www.cardekho.com/overview/Ford_Endeavour/Ford_Endeavour_2.2_Trend_AT_4X2.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Tata_Sumo/Tata_Sumo_Gold_CX.htm', 'https://www.cardekho.com/overview/Jeep_Grand_Cherokee/Jeep_Grand_Cherokee_Limited_4X4.htm', 'https://www.cardekho.com/overview/Hyundai_Santa_Fe/Hyundai_Santa_Fe_2WD_AT.htm', 'https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Titanium_BE.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Mitsubishi_Pajero/Mitsubishi_Pajero_Sport_4X4_Dual_Tone.htm', 'https://www.cardekho.com/overview/Maruti_SX4_S_Cross/Maruti_SX4_S_Cross_DDiS_200_Sigma.htm', 'https://www.cardekho.com/overview/Premier_Rio/Premier_Rio_LX.htm', 'https://www.cardekho.com/overview/Mahindra_Bolero/Mahindra_Bolero_SLE_BSIII.htm', 'https://www.cardekho.com/overview/Honda_BR-V/Honda_BR-V_i-DTEC_S_MT.htm', 'https://www.cardekho.com/overview/Nissan_Terrano/Nissan_Terrano_XE_85_PS.htm', 'https://www.cardekho.com/overview/Force_Gurkha/Force_Gurkha_Soft_Top_BS3_4WD.htm', 'https://www.cardekho.com/overview/Tata_Safari_Storme/Tata_Safari_Storme_LX.htm', 'https://www.cardekho.com/overview/Audi_Q5/Audi_Q5_30_TDI_quattro_Premium.htm']
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
		pickle.dump(g,open("variant_suv_output.p","wb"))
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