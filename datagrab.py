from bs4 import BeautifulSoup
import urllib
import re

variants_dict = {'Tata Bolt Revotron XE': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XE.htm', 'Ford Figo 1.5P Titanium AT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5P_Titanium_AT.htm', 'Maruti Wagon R Stingray LXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_LXI.htm', 'Datsun GO D': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_D.htm', 'Ford Figo 1.5D Trend MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Trend_MT.htm', 'Hyundai Grand i10 Magna': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Magna.htm', 'Maruti Baleno 1.3 Zeta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Zeta.htm', 'Datsun GO A': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_A.htm', 'Hyundai Grand i10 Magna AT': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Magna_AT.htm', 'Volkswagen Polo 1.2 MPI Trendline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Trendline.htm', 'Tata Bolt Revotron XT': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XT.htm', 'Hyundai Grand i10 CRDi Sportz Celebration Edition': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Sportz_Celebration_Edition.htm', 'Maruti Celerio VDi': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VDi.htm', 'Tata Bolt Quadrajet XE': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XE.htm', 'Datsun GO T': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_T.htm', 'Nissan Micra Active XL': 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XL.htm', 'Tata Tiago 1.05 Revotorq XZ WO Alloy': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XZ_WO_Alloy.htm', 'Ford Figo 1.5D Titanium MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Titanium_MT.htm', 'Chevrolet Sail Hatchback 1.3 TCDi LS ABS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LS_ABS.htm', 'Chevrolet Beat LT': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LT.htm', 'Honda Jazz 1.2 S AT i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_S_AT_i_VTEC.htm', 'Tata Tiago 1.2 Revotron XZ WO Alloy': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XZ_WO_Alloy.htm', 'Hyundai Elite i20 Sportz 1.4 CRDi': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Sportz_1.4_CRDi.htm', 'Maruti Alto 800 VXI Optional': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_VXI_Optional.htm', 'Fiat Avventura Power Up 1.3 Dynamic': 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Dynamic.htm', 'Honda Brio 1.2 VX AT': 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_VX_AT.htm', 'Honda Jazz 1.5 S i DTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_S_i_DTEC.htm', 'Fiat Avventura Urban Cross 1.4 T-Jet Emotion': 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.4_T-Jet_Emotion.htm', 'Datsun Redi GO Sport': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_Sport.htm', 'Chevrolet Sail Hatchback 1.2 LS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LS.htm', 'Volkswagen Beetle 1.4 TSI': 'https://www.cardekho.com/overview/Volkswagen_Beetle/Volkswagen_Beetle_1.4_TSI.htm', 'Hyundai i20 Active 1.2': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2.htm', 'Honda Brio 1.2 E MT': 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_E_MT.htm', 'Volkswagen CrossPolo 1.2 MPI': 'https://www.cardekho.com/overview/Volkswagen_CrossPolo/Volkswagen_CrossPolo_1.2_MPI.htm', 'Toyota Etios Cross 1.2L G': 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.2L_G.htm', 'Volkswagen Polo Select 1.5 TDI Highline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_Select_1.5_TDI_Highline.htm', 'Renault KWID 1.0 RXT Optional': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_1.0_RXT_Optional.htm', 'Maruti Wagon R AMT VXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_AMT_VXI.htm', 'Toyota Etios Liva 1.2 V': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_V.htm', 'Maruti Celerio ZDi': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZDi.htm', 'Fiat Punto EVO Power UP 1.3 Emotion': 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Emotion.htm', 'Maruti Wagon R VXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_VXI_BS_IV.htm', 'Hyundai Grand i10 CRDi Era': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Era.htm', 'Nissan Micra XV CVT': 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_AT.htm', 'Maruti Alto K10 LXI CNG Optional': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_CNG_Optional.htm', 'Tata Bolt Quadrajet XM': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XM.htm', 'Maruti Alto K10 LXI': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI.htm', 'Chevrolet Spark 1.0': 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0.htm', 'Hyundai i20 Active 1.4': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4.htm', 'Renault KWID STD': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_STD.htm', 'Tata Tiago 1.2 Revotron XT Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XT_Option.htm', 'Maruti Ritz LXi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_LXi.htm', 'Hyundai Elite i20 Asta Option 1.2': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_Option_1.2.htm', 'Maruti Wagon R Stingray AMT VXI Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_AMT_VXI_Optional.htm', 'Hyundai Elite i20 Asta 1.4 CRDi': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_1.4_CRDi.htm', 'Maruti Swift VDI': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_BS_IV.htm', 'Maruti Celerio LXI AT Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_AT_Optional.htm', 'Fiat Avventura Urban Cross 1.3 Multijet Active': 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.3_Multijet_Active.htm', 'Renault Pulse Petrol RxL': 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_Petrol_RxL.htm', 'Hyundai Grand i10 Sportz Celebration Edition': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Sportz_Celebration_Edition.htm', 'Honda Jazz 1.5 E i DTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_E_i_DTEC.htm', 'Honda Brio 1.2 VX MT': 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_VX_MT.htm', 'Maruti Swift LXI': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI.htm', 'Hyundai Grand i10 Asta Option AT': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Asta_Option_AT.htm', 'Maruti Ritz ZXi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_ZXi.htm', 'Tata Tiago 1.05 Revotorq XE Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XE_Option.htm', 'Maruti Ritz VXi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VXi.htm', 'Tata Indica eV2 eLX': 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_eLX.htm', 'Chevrolet Beat LTZ': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LTZ.htm', 'Tata Indica eV2 DLX BSIII': 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_DLX_BSIII.htm', 'Chevrolet Sail Hatchback 1.3 TCDi LT ABS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LT_ABS.htm', 'Renault KWID 1.0 RXT': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_1.0.htm', 'Maruti Celerio VXI AT': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_AT.htm', 'Datsun Redi GO T Option': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_T_Option.htm', 'Tata Tiago 1.05 Revotorq XM': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XM.htm', 'Honda Jazz 1.5 V i DTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_V_i_DTEC.htm', 'Fiat Avventura Power Up 1.3 Emotion': 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Emotion.htm', 'Tata Tiago 1.05 Revotorq XE': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XE.htm', 'Tata Tiago 1.2 Revotron XM Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XM_Option.htm', 'Maruti Wagon R Stingray LXI Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_LXI_Optional.htm', 'Tata Tiago 1.05 Revotorq XB': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XB.htm', 'Maruti Alto 800 VXI': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_VXI.htm', 'Maruti Alto K10 VXI': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI.htm', 'Renault KWID RXT Driver Airbag Option': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXT_Optional.htm', 'Maruti Swift VXI Glory Limited Edition': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Glory_Limited_Edition.htm', 'Volkswagen Polo 1.5 TDI Comfortline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Comfortline.htm', 'Tata Tiago 1.05 Revotorq XZ': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XZ.htm', 'Fiat Punto Pure 1.3L Advanced Multi-Jet': 'https://www.cardekho.com/overview/Fiat_Punto_Pure/Fiat_Punto_Pure_1.3L_Advanced_Multi-Jet.htm', 'Tata Tiago 1.05 Revotorq XT': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XT.htm', 'Chevrolet Beat Diesel LT': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LT.htm', 'Nissan Micra Diesel XL Optional': 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_Diesel_XL_Optional.htm', 'Maruti Celerio ZDi Option': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZDi_Option.htm', 'Chevrolet Beat Diesel LS': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LS.htm', 'Hyundai Elite i20 Magna 1.4 CRDi': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_1.4_CRDi.htm', 'Tata Tiago 1.05 Revotorq XT Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XT_Option.htm', 'Fiat Abarth Avventura 1.4 T-Jet': 'https://www.cardekho.com/overview/Fiat_Abarth_Avventura/Fiat_Abarth_Avventura_1.4_T-Jet.htm', 'Hyundai i20 Active 1.2 S': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2_S.htm', 'Maruti Ritz VDi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VDi.htm', 'Maruti Celerio LXI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_Optional.htm', 'Volvo V40 Cross Country T4': 'https://www.cardekho.com/overview/Volvo_V40_Cross_Country/Volvo_V40_Cross_Country_T4.htm', 'Maruti Ritz VXi (ABS)': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VXi_(ABS)_BS_IV.htm', 'Maruti Swift ZXI': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_ZXI.htm', 'Nissan Micra Diesel XL': 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_Diesel_XL.htm', 'Hyundai EON 1.0 Kappa Magna Plus Optional': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_1.0_Kappa_Magna_Plus_Optional.htm', 'Hyundai Grand i10 CRDi Magna': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Magna.htm', 'Maruti Swift VDI Glory Limited Edition': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Glory_Limited_Edition.htm', 'Hyundai i10 Sportz 1.1L': 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Sportz_1.1L.htm', 'Maruti Celerio Green VXI': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_Green_VXI.htm', 'Maruti Baleno 1.2 CVT Zeta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_CVT_Zeta.htm', 'Mini 5 DOOR Cooper D': 'https://www.cardekho.com/overview/Mini_5_DOOR/Mini_5_DOOR_Cooper_D.htm', 'Ford Figo 1.2P Base MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Base_MT.htm', 'Hyundai i10 Magna 1.1L': 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Magna_1.1L.htm', 'Datsun GO T Option': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_T_Option.htm', 'Maruti Celerio ZXI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_Optional.htm', 'Mini 3 DOOR Cooper D': 'https://www.cardekho.com/overview/Mini_3_DOOR/Mini_3_DOOR_Cooper_D.htm', 'Toyota Etios Liva 1.4 VD': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_VD.htm', 'Maruti Swift VXI Deca': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Deca.htm', 'Hyundai i20 Active 1.4 SX with AVN': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4_SX_with_AVN.htm', 'Tata Bolt Quadrajet XMS': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XMS.htm', 'Mini 3 DOOR Cooper S': 'https://www.cardekho.com/overview/Mini_3_DOOR/Mini_3_DOOR_Cooper_S.htm', 'Maruti Swift LDI Optional': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LDI_Optional.htm', 'Chevrolet Beat PS': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_PS.htm', 'Maruti Celerio LXI': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI.htm', 'Ford Figo 1.5D Titanium Plus MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Titanium_Plus_MT.htm', 'Fiat Punto EVO Power Up 1.2 Dynamic': 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_Up_1.2_Dynamic.htm', 'Chevrolet Sail Hatchback 1.3 TCDi LS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi_LS.htm', 'Hyundai Grand i10 Asta Option': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Asta_Option.htm', 'Maruti Baleno 1.2 CVT Delta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_CVT_Delta.htm', 'Tata Tiago 1.2 Revotron XE': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XE.htm', 'Tata Tiago 1.2 Revotron XB': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XB.htm', 'Toyota Etios Cross 1.5L V': 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.5L_V.htm', 'Volkswagen CrossPolo 1.5 TDI': 'https://www.cardekho.com/overview/Volkswagen_CrossPolo/Volkswagen_CrossPolo_1.5_TDI.htm', 'Maruti Celerio ZXI AT': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_AT.htm', 'Honda Brio 1.2 S MT': 'https://www.cardekho.com/overview/Honda_Brio/Honda_Brio_1.2_S_MT.htm', 'Tata Tiago 1.2 Revotron XM': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XM.htm', 'Renault Pulse RxZ': 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_RxZ.htm', 'Tata Bolt Revotron XMS': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XMS.htm', 'Maruti Swift LDI': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LDI_BSIV.htm', 'Tata Tiago 1.2 Revotron XT': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XT.htm', 'Hyundai Elite i20 Sportz 1.2': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Sportz_1.2.htm', 'Maruti Swift ZDi': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_ZDi.htm', 'Hyundai Elite i20 Era 1.4 CRDi': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Era_1.4_CRDi.htm', 'Fiat Abarth Punto EVO 1.4 T-Jet': 'https://www.cardekho.com/overview/Fiat_Punto_Abarth/Fiat_Punto_Abarth_1.4_T-Jet.htm', 'Mercedes-Benz A-Class A200 D Sport': 'https://www.cardekho.com/overview/Mercedes-Benz_A_Class/Mercedes-Benz_A_Class_A200_D_Sport.htm', 'Hyundai EON Sportz': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Sportz.htm', 'Volvo V40 D3 R-Design': 'https://www.cardekho.com/overview/Volvo_V40/Volvo_V40_D3_R_Design.htm', 'Tata Tiago 1.2 Revotron XZ': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XZ.htm', 'Hyundai Grand i10 CRDi Asta Option': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Asta_Option.htm', 'Hyundai Grand i10 Era': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Era.htm', 'Hyundai Elite i20 Magna AT 1.4': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_AT_1.4.htm', 'Toyota Etios Liva 1.2 GX': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_G.htm', 'Chevrolet Beat LS': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_LS.htm', 'Mahindra e2o T2': 'https://www.cardekho.com/overview/Mahindra_e2o/Mahindra_e2o_T2.htm', 'Hyundai i10 Era': 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Era.htm', 'Maruti Swift VXI': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI.htm', 'Hyundai EON D Lite': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite.htm', 'Volkswagen Polo 1.2 MPI Comfortline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Comfortline.htm', 'Maruti Ritz LDi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_LDi.htm', 'Tata Nano CNG XM': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_CNG_XM.htm', 'Hyundai EON 1.0 Magna Plus Option O': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_1.0_Magna_Plus_Option_O.htm', 'Honda Jazz 1.2 VX i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_VX_i_VTEC.htm', 'Volkswagen Polo GT TSI': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_GT_TSI.htm', 'Hyundai i20 Active 1.4 S': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.4_S.htm', 'Hyundai Elite i20 Asta Option 1.4 CRDi': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_Option_1.4_CRDi.htm', 'Hyundai EON Magna Plus Option': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Magna_Plus_Option.htm', 'Maruti Alto 800 LXI': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LXI.htm', 'Honda Jazz 1.5 VX i DTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_VX_i_DTEC.htm', 'Maruti Swift 1.3 DLX': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_1.3_DLX.htm', 'Toyota Etios Cross 1.4L VD': 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.4L_VD.htm', 'Hyundai Elite i20 Magna 1.2': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Magna_1.2.htm', 'Honda Jazz 1.2 E i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_E_i_VTEC.htm', 'Datsun GO A EPS': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_A_EPS.htm', 'Tata Tiago 1.05 Revotorq XM Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.05_Revotorq_XM_Option.htm', 'Fiat Avventura Power Up 1.3 Active': 'https://www.cardekho.com/overview/Fiat_Avventura/Fiat_Avventura_Power_Up_1.3_Active.htm', 'Maruti Alto K10 VXI AGS': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_AMT.htm', 'Maruti Alto 800 CNG LXI': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_CNG_LXI.htm', 'Tata Nano XMA': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XMA.htm', 'Maruti Wagon R Stingray VXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_VXI.htm', 'Hyundai EON LPG Era Plus': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Era_Plus.htm', 'Nissan Micra XL CVT': 'https://www.cardekho.com/overview/Nissan_Micra/Nissan_Micra_XL_CVT.htm', 'Honda Jazz 1.5 SV i DTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.5_SV_i_DTEC.htm', 'Maruti Celerio VDI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VDI_Optional.htm', 'Honda Jazz 1.2 V AT i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_V_AT_i_VTEC.htm', 'Maruti Baleno 1.2 Sigma': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Sigma.htm', 'Chevrolet Sail Hatchback 1.2 LS ABS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LS_ABS.htm', 'Maruti Baleno 1.3 Alpha': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Alpha.htm', 'Tata Tiago 1.2 Revotron XE Option': 'https://www.cardekho.com/overview/Tata_Tiago/Tata_Tiago_1.2_Revotron_XE_Option.htm', 'Nissan Micra Active XV': 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XV.htm', 'Maruti Swift VDI Deca': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Deca.htm', 'Maruti Alto K10 LX': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LX.htm', 'Maruti Alto K10 LXI Optional': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_Optional.htm', 'Fiat Punto Pure 1.2L FIRE': 'https://www.cardekho.com/overview/Fiat_Punto_Pure/Fiat_Punto_Pure_1.2L_FIRE.htm', 'Maruti Alto 800 LX Optional': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LX_Optional.htm', 'Maruti Swift LXI Option': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI_Option.htm', 'Toyota Etios Liva 1.4 GXD': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_GD.htm', 'Ford Figo 1.5D Ambiente MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Ambiente_MT.htm', 'Maruti Celerio VXI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_Optional.htm', 'Maruti Baleno 1.2 Zeta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Zeta.htm', 'Tata Indica eV2 eLS': 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_eLS.htm', 'Maruti Wagon R AMT VXI Option': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_AMT_VXI_Option.htm', 'Hyundai Elite i20 Era 1.2': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Era_1.2.htm', 'Maruti Celerio ZXI AT Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI_AT_Optional.htm', 'Hyundai EON Era Plus Option': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Era_Plus_Option.htm', 'Volkswagen Polo Select 1.2 MPI Highline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_Select_1.2_MPI_Highline.htm', 'Hyundai EON Era Plus': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Era_Plus.htm', 'Toyota Etios Cross 1.4L GD': 'https://www.cardekho.com/overview/Toyota_Etios_Cross/Toyota_Etios_Cross_1.4L_GD.htm', 'Toyota Etios Liva 1.4 VXD': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.4_VXD.htm', 'Toyota Etios Liva 1.2 VX': 'https://www.cardekho.com/overview/Toyota_Etios_Liva/Toyota_Etios_Liva_1.2_VX.htm', 'Ford Figo 1.2P Titanium MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Titanium_MT.htm', 'Volkswagen Polo 1.5 TDI Highline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Highline.htm', 'Ford Figo 1.2P Titanium Plus MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Titanium_Plus_MT.htm', 'Honda Jazz 1.2 SV i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_SV_i_VTEC.htm', 'Tata Nano XTA': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XTA.htm', 'Maruti Celerio ZXI': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_ZXI.htm', 'Mini Countryman Cooper D': 'https://www.cardekho.com/overview/Mini_Cooper_Countryman/Mini_Cooper_Countryman_Cooper_D.htm', 'Maruti Alto K10 LXI CNG': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LXI_CNG.htm', 'Chevrolet Beat Diesel PS': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_PS.htm', 'Chevrolet Sail Hatchback 1.3 TCDi': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.3_TCDi.htm', 'Renault Pulse RxL ABS': 'https://www.cardekho.com/overview/Renault_Pulse/Renault_Pulse_RxL_Optional.htm', 'Tata Bolt Revotron XM': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Revotron_XM.htm', 'Tata Nano XM': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XM.htm', 'Volkswagen Polo 1.2 MPI Highline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.2_MPI_Highline.htm', 'Hyundai Grand i10 Sportz': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_Sportz.htm', 'Fiat Avventura Urban Cross 1.3 Multijet Dynamic': 'https://www.cardekho.com/overview/Fiat_Avventura_Urban_Cross/Fiat_Avventura_Urban_Cross_1.3_Multijet_Dynamic.htm', 'Tata Indica eV2 LS BSIII': 'https://www.cardekho.com/overview/Tata_Indica_V2/Tata_Indica_V2_DLS_BSIII.htm', 'Maruti Celerio VXI AT Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI_AT_Optional.htm', 'Tata Nano XE': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XE.htm', 'Maruti Alto 800 CNG LXI Optional': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_CNG_LXI_Optional.htm', 'Ford Figo 1.5D Base MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.5D_Base_MT.htm', 'Maruti Wagon R VXI Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_VXI_Optional.htm', 'Maruti Wagon R Stingray AMT VXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_AMT_VXI.htm', 'Maruti Ritz ZDi': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_ZDi.htm', 'Mercedes-Benz A-Class A180 Sport': 'https://www.cardekho.com/overview/Mercedes-Benz_A_Class/Mercedes-Benz_A_Class_A180_Sport.htm', 'Maruti Ritz AT': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_AT.htm', 'Maruti Swift 1.2 DLX': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_1.2_DLX.htm', 'Hyundai Grand i10 CRDi Sportz': 'https://www.cardekho.com/overview/Hyundai_Grand_i10/Hyundai_Grand_i10_CRDi_Sportz.htm', 'Tata Nano XT': 'https://www.cardekho.com/overview/Tata_Nano/Tata_Nano_XT.htm', 'Chevrolet Beat Diesel LTZ': 'https://www.cardekho.com/overview/Chevrolet_Beat/Chevrolet_Beat_Diesel_LTZ.htm', 'Maruti Wagon R LXI': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_BS_IV.htm', 'Maruti Swift LXI Optional-O': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_LXI_Optional-O.htm', 'Maruti Alto K10 VXI AGS Optional': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_AGS_Optional.htm', 'Hyundai EON LPG Era Plus Option': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Era_Plus_Option.htm', 'Hyundai i10 Sportz 1.1L LPG': 'https://www.cardekho.com/overview/Hyundai_i10/Hyundai_i10_Sportz_1.1L_LPG.htm', 'Volkswagen Polo GT 1.5 TDI': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_GT_1.5_TDI.htm', 'Chevrolet Sail Hatchback 1.2 LT ABS': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2_LT_ABS.htm', 'Chevrolet Sail Hatchback 1.2': 'https://www.cardekho.com/overview/Chevrolet_Sail_Hatchback/Chevrolet_Sail_Hatchback_1.2.htm', 'Datsun Redi GO T': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_T.htm', 'Datsun Redi GO S': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_S.htm', 'Fiat 500 Abarth 595 Competizione': 'https://www.cardekho.com/overview/Fiat_500/Fiat_500_Abarth_595_Competizione.htm', 'Maruti Baleno 1.3 Sigma': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Sigma.htm', 'Tata Bolt Quadrajet XT': 'https://www.cardekho.com/overview/Tata_Bolt/Tata_Bolt_Quadrajet_XT.htm', 'Maruti Wagon R LXI CNG': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_CNG.htm', 'Renault KWID RXE': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXE.htm', 'Maruti Alto K10 LX Optional': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_LX_Optional.htm', 'Datsun Redi GO D': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_D.htm', 'Renault KWID RXL': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXL.htm', 'Hyundai EON LPG Magna Plus': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_LPG_Magna_Plus.htm', 'Datsun Redi GO A': 'https://www.cardekho.com/overview/Datsun_RediGO/Datsun_RediGO_A.htm', 'Hyundai EON D Lite Plus': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite_Plus.htm', 'Maruti Alto K10 VXI Option': 'https://www.cardekho.com/overview/Maruti_Alto_K10/Maruti_Alto_K10_VXI_Airbag.htm', 'Maruti Alto 800 LXI Optional': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LXI_Optional.htm', 'Maruti Baleno 1.3 Delta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.3_Delta.htm', 'Datsun GO Style': 'https://www.cardekho.com/overview/Datsun_GO/Datsun_GO_Style.htm', 'Hyundai i20 Active 1.2 SX with AVN': 'https://www.cardekho.com/overview/Hyundai_i20_Active/Hyundai_i20_Active_1.2_SX_with_AVN.htm', 'Nissan Micra Active XV S': 'https://www.cardekho.com/overview/Nissan_Micra_Active/Nissan_Micra_Active_XV_S.htm', 'BMW 1 Series 118d Sport Line': 'https://www.cardekho.com/overview/BMW_1_Series/BMW_1_Series_118d_Sport_Line.htm', 'Hyundai EON Magna Plus': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_Magna_Plus.htm', 'Maruti Ritz VDI (ABS)': 'https://www.cardekho.com/overview/Maruti_Ritz/Maruti_Ritz_VDI_(ABS)_BS_IV.htm', 'Honda Jazz 1.2 S i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_S_i_VTEC.htm', 'Maruti Alto 800 STD Optional': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_Std_Optional.htm', 'Maruti Alto 800 LX': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_LX.htm', 'Maruti Baleno 1.2 Delta': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Delta.htm', 'Fiat Punto EVO Power UP 1.3 Active': 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Active.htm', 'Volvo V40 D3 Kinetic': 'https://www.cardekho.com/overview/Volvo_V40/Volvo_V40_D3.htm', 'Renault KWID RXT': 'https://www.cardekho.com/overview/Renault_KWID/Renault_KWID_RXT.htm', 'Chevrolet Spark 1.0 LT': 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0_LT.htm', 'Maruti Celerio LDI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LDI_Optional.htm', 'Chevrolet Spark 1.0 LS': 'https://www.cardekho.com/overview/Chevrolet_Spark/Chevrolet_Spark_1.0_LS.htm', 'Maruti Celerio LDi': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LDi.htm', 'Hyundai EON D Lite Plus Option': 'https://www.cardekho.com/overview/Hyundai_EON/Hyundai_EON_D_Lite_Plus_Option.htm', 'Maruti Celerio Green VXI Optional': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_Green_VXI_Optional.htm', 'Mahindra Verito Vibe 1.5 dCi D2': 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D2.htm', 'Maruti Alto 800 STD': 'https://www.cardekho.com/overview/Maruti_Alto_800/Maruti_Alto_800_STD.htm', 'Fiat Punto EVO Power UP 1.3 Dynamic': 'https://www.cardekho.com/overview/Fiat_Grande_Punto/Fiat_Grande_Punto_EVO_Power_UP_1.3_Dynamic.htm', 'Mahindra Verito Vibe 1.5 dCi D6': 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D6.htm', 'Maruti Swift VDI Optional': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_Optional.htm', 'Maruti Wagon R Stingray VXI Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R_Stingray/Maruti_Wagon_R_Stingray_VXI_Optional.htm', 'Maruti Wagon R LXI Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_Optional.htm', 'Maruti Celerio VXI': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_VXI.htm', 'Maruti Baleno 1.2 Alpha': 'https://www.cardekho.com/overview/Maruti_Baleno/Maruti_Baleno_1.2_Alpha.htm', 'Volkswagen Polo 1.5 TDI Trendline': 'https://www.cardekho.com/overview/Volkswagen_Polo/Volkswagen_Polo_1.5_TDI_Trendline.htm', 'Maruti Wagon R LXI CNG Optional': 'https://www.cardekho.com/overview/Maruti_Wagon_R/Maruti_Wagon_R_LXI_CNG_Optional.htm', 'Mahindra Verito Vibe 1.5 dCi D4': 'https://www.cardekho.com/overview/Mahindra_Verito_Vibe/Mahindra_Verito_Vibe_1.5_dCi_D4.htm', 'Honda Jazz 1.2 V i VTEC': 'https://www.cardekho.com/overview/Honda_Jazz/Honda_Jazz_1.2_V_i_VTEC.htm', 'Maruti Celerio LXI AT': 'https://www.cardekho.com/overview/Maruti_Celerio/Maruti_Celerio_LXI_AT.htm', 'Maruti Swift VXI Optional': 'https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VXI_Optional.htm', 'Hyundai Elite i20 Asta 1.2': 'https://www.cardekho.com/overview/Hyundai_i20/Hyundai_i20_Asta_1.2.htm', 'Ford Figo 1.2P Trend MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Trend_MT.htm', 'Ford Figo 1.2P Ambiente MT': 'https://www.cardekho.com/overview/Ford_Figo/Ford_Figo_1.2P_Ambiente_MT.htm'}

for url in variants_dict.values():
	try:
		page = urllib.urlopen(url)
		soup = BeautifulSoup(page.read())
		soup=soup.find("div", {"id": "descriptionReadMore"})
		for node in soup.findAll('p'):
				print '\n'.join(node.findAll(text=True))
	except Exception as e:
		print url