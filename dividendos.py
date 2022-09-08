
import yfinance as yf
import pandas as pd
import numpy as np

cods = [
 {
  "cod_b3": "SYNE3",
  "cod_y": "SYNE3.SA"
 },
 {
  "cod_b3": "CEBR5",
  "cod_y": "CEBR5.SA"
 },
 {
  "cod_b3": "CEBR6",
  "cod_y": "CEBR6.SA"
 },
 {
  "cod_b3": "CEBR3",
  "cod_y": "CEBR3.SA"
 },
 {
  "cod_b3": "PETR4",
  "cod_y": "PETR4.SA"
 },
 {
  "cod_b3": "CALI3",
  "cod_y": "CALI3.SA"
 },
 {
  "cod_b3": "PETR3",
  "cod_y": "PETR3.SA"
 },
 {
  "cod_b3": "PETR3",
  "cod_y": "PETR3.SA"
 },
 {
  "cod_b3": "EEEL3",
  "cod_y": "EEEL3.SA"
 },
 {
  "cod_b3": "GPAR3",
  "cod_y": "GPAR3.SA"
 },
 {
  "cod_b3": "BRAP4",
  "cod_y": "BRAP4.SA"
 },
 {
  "cod_b3": "EEEL4",
  "cod_y": "EEEL4.SA"
 },
 {
  "cod_b3": "BRAP3",
  "cod_y": "BRAP3.SA"
 },
 {
  "cod_b3": "MRFG3",
  "cod_y": "MRFG3.SA"
 },
 {
  "cod_b3": "BRKM5",
  "cod_y": "BRKM5.SA"
 },
 {
  "cod_b3": "BRKM3",
  "cod_y": "BRKM3.SA"
 },
 {
  "cod_b3": "LAVV3",
  "cod_y": "LAVV3.SA"
 },
 {
  "cod_b3": "GOAU3",
  "cod_y": "GOAU3.SA"
 },
 {
  "cod_b3": "GOAU4",
  "cod_y": "GOAU4.SA"
 },
 {
  "cod_b3": "VALE3",
  "cod_y": "VALE3.SA"
 },
 {
  "cod_b3": "CEEB5",
  "cod_y": "CEEB5.SA"
 },
 {
  "cod_b3": "CSRN5",
  "cod_y": "CSRN5.SA"
 },
 {
  "cod_b3": "CSRN6",
  "cod_y": "CSRN6.SA"
 },
 {
  "cod_b3": "PEAB3",
  "cod_y": "PEAB3.SA"
 },
 {
  "cod_b3": "CEEB3",
  "cod_y": "CEEB3.SA"
 },
 {
  "cod_b3": "CSRN3",
  "cod_y": "CSRN3.SA"
 },
 {
  "cod_b3": "SOND5",
  "cod_y": "SOND5.SA"
 },
 {
  "cod_b3": "UNIP3",
  "cod_y": "UNIP3.SA"
 },
 {
  "cod_b3": "PEAB4",
  "cod_y": "PEAB4.SA"
 },
 {
  "cod_b3": "UNIP5",
  "cod_y": "UNIP5.SA"
 },
 {
  "cod_b3": "GGBR3",
  "cod_y": "GGBR3.SA"
 },
 {
  "cod_b3": "EKTR4",
  "cod_y": "EKTR4.SA"
 },
 {
  "cod_b3": "LEVE3",
  "cod_y": "LEVE3.SA"
 },
 {
  "cod_b3": "UNIP6",
  "cod_y": "UNIP6.SA"
 },
 {
  "cod_b3": "CPLE6",
  "cod_y": "CPLE6.SA"
 },
 {
  "cod_b3": "CPLE11",
  "cod_y": "CPLE11.SA"
 },
 {
  "cod_b3": "EKTR3",
  "cod_y": "EKTR3.SA"
 },
 {
  "cod_b3": "EALT4",
  "cod_y": "EALT4.SA"
 },
 {
  "cod_b3": "EPAR3",
  "cod_y": "EPAR3.SA"
 },
 {
  "cod_b3": "AGRO3",
  "cod_y": "AGRO3.SA"
 },
 {
  "cod_b3": "CPLE3",
  "cod_y": "CPLE3.SA"
 },
 {
  "cod_b3": "SOND6",
  "cod_y": "SOND6.SA"
 },
 {
  "cod_b3": "CMIN3",
  "cod_y": "CMIN3.SA"
 },
 {
  "cod_b3": "COCE6",
  "cod_y": "COCE6.SA"
 },
 {
  "cod_b3": "ALLD3",
  "cod_y": "ALLD3.SA"
 },
 {
  "cod_b3": "GGBR4",
  "cod_y": "GGBR4.SA"
 },
 {
  "cod_b3": "BAZA3",
  "cod_y": "BAZA3.SA"
 },
 {
  "cod_b3": "EALT3",
  "cod_y": "EALT3.SA"
 },
 {
  "cod_b3": "SOND3",
  "cod_y": "SOND3.SA"
 },
 {
  "cod_b3": "CGAS5",
  "cod_y": "CGAS5.SA"
 },
 {
  "cod_b3": "BMGB4",
  "cod_y": "BMGB4.SA"
 },
 {
  "cod_b3": "MYPK3",
  "cod_y": "MYPK3.SA"
 },
 {
  "cod_b3": "DXCO3",
  "cod_y": "DXCO3.SA"
 },
 {
  "cod_b3": "TAEE11",
  "cod_y": "TAEE11.SA"
 },
 {
  "cod_b3": "TAEE4",
  "cod_y": "TAEE4.SA"
 },
 {
  "cod_b3": "TAEE3",
  "cod_y": "TAEE3.SA"
 },
 {
  "cod_b3": "CGAS3",
  "cod_y": "CGAS3.SA"
 },
 {
  "cod_b3": "TKNO4",
  "cod_y": "TKNO4.SA"
 },
 {
  "cod_b3": "CMIG4",
  "cod_y": "CMIG4.SA"
 },
 {
  "cod_b3": "TKNO3",
  "cod_y": "TKNO3.SA"
 },
 {
  "cod_b3": "CEPE6",
  "cod_y": "CEPE6.SA"
 },
 {
  "cod_b3": "CLSC3",
  "cod_y": "CLSC3.SA"
 },
 {
  "cod_b3": "CPFE3",
  "cod_y": "CPFE3.SA"
 },
 {
  "cod_b3": "CEPE5",
  "cod_y": "CEPE5.SA"
 },
 {
  "cod_b3": "CRPG5",
  "cod_y": "CRPG5.SA"
 },
 {
  "cod_b3": "ENAT3",
  "cod_y": "ENAT3.SA"
 },
 {
  "cod_b3": "CRPG6",
  "cod_y": "CRPG6.SA"
 },
 {
  "cod_b3": "MELK3",
  "cod_y": "MELK3.SA"
 },
 {
  "cod_b3": "USIM5",
  "cod_y": "USIM5.SA"
 },
 {
  "cod_b3": "CLSC4",
  "cod_y": "CLSC4.SA"
 },
 {
  "cod_b3": "ENBR3",
  "cod_y": "ENBR3.SA"
 },
 {
  "cod_b3": "TASA4",
  "cod_y": "TASA4.SA"
 },
 {
  "cod_b3": "MOVI3",
  "cod_y": "MOVI3.SA"
 },
 {
  "cod_b3": "BEES3",
  "cod_y": "BEES3.SA"
 },
 {
  "cod_b3": "MOAR3",
  "cod_y": "MOAR3.SA"
 },
 {
  "cod_b3": "GETT4",
  "cod_y": "GETT4.SA"
 },
 {
  "cod_b3": "BEES4",
  "cod_y": "BEES4.SA"
 },
 {
  "cod_b3": "TASA3",
  "cod_y": "TASA3.SA"
 },
 {
  "cod_b3": "GETT11",
  "cod_y": "GETT11.SA"
 },
 {
  "cod_b3": "CRIV4",
  "cod_y": "CRIV4.SA"
 },
 {
  "cod_b3": "USIM3",
  "cod_y": "USIM3.SA"
 },
 {
  "cod_b3": "BNBR3",
  "cod_y": "BNBR3.SA"
 },
 {
  "cod_b3": "ENGI4",
  "cod_y": "ENGI4.SA"
 },
 {
  "cod_b3": "VIVT3",
  "cod_y": "VIVT3.SA"
 },
 {
  "cod_b3": "BRGE6",
  "cod_y": "BRGE6.SA"
 },
 {
  "cod_b3": "BBAS3",
  "cod_y": "BBAS3.SA"
 },
 {
  "cod_b3": "BSLI4",
  "cod_y": "BSLI4.SA"
 },
 {
  "cod_b3": "BRIV4",
  "cod_y": "BRIV4.SA"
 },
 {
  "cod_b3": "AURA33",
  "cod_y": "AURA33.SA"
 },
 {
  "cod_b3": "SANB4",
  "cod_y": "SANB4.SA"
 },
 {
  "cod_b3": "SANB11",
  "cod_y": "SANB11.SA"
 },
 {
  "cod_b3": "GETT3",
  "cod_y": "GETT3.SA"
 },
 {
  "cod_b3": "SANB3",
  "cod_y": "SANB3.SA"
 },
 {
  "cod_b3": "CRIV3",
  "cod_y": "CRIV3.SA"
 },
 {
  "cod_b3": "RAPT3",
  "cod_y": "RAPT3.SA"
 },
 {
  "cod_b3": "RANI3",
  "cod_y": "RANI3.SA"
 },
 {
  "cod_b3": "REDE3",
  "cod_y": "REDE3.SA"
 },
 {
  "cod_b3": "PTBL3",
  "cod_y": "PTBL3.SA"
 },
 {
  "cod_b3": "CGRA4",
  "cod_y": "CGRA4.SA"
 },
 {
  "cod_b3": "CGRA3",
  "cod_y": "CGRA3.SA"
 },
 {
  "cod_b3": "BRGE11F",
  "cod_y": "BRGE11F.SA"
 },
 {
  "cod_b3": "CMIG3",
  "cod_y": "CMIG3.SA"
 },
 {
  "cod_b3": "BRBI11",
  "cod_y": "BRBI11.SA"
 },
 {
  "cod_b3": "BRSR6",
  "cod_y": "BRSR6.SA"
 },
 {
  "cod_b3": "RAPT4",
  "cod_y": "RAPT4.SA"
 },
 {
  "cod_b3": "RPAD5",
  "cod_y": "RPAD5.SA"
 },
 {
  "cod_b3": "ENGI11",
  "cod_y": "ENGI11.SA"
 },
 {
  "cod_b3": "SMTO3",
  "cod_y": "SMTO3.SA"
 },
 {
  "cod_b3": "ETER3",
  "cod_y": "ETER3.SA"
 },
 {
  "cod_b3": "WHRL4",
  "cod_y": "WHRL4.SA"
 },
 {
  "cod_b3": "WIZS3",
  "cod_y": "WIZS3.SA"
 },
 {
  "cod_b3": "KLBN11",
  "cod_y": "KLBN11.SA"
 },
 {
  "cod_b3": "WHRL3",
  "cod_y": "WHRL3.SA"
 },
 {
  "cod_b3": "KLBN3",
  "cod_y": "KLBN3.SA"
 },
 {
  "cod_b3": "KLBN4",
  "cod_y": "KLBN4.SA"
 },
 {
  "cod_b3": "PFRM3",
  "cod_y": "PFRM3.SA"
 },
 {
  "cod_b3": "BRSR3",
  "cod_y": "BRSR3.SA"
 },
 {
  "cod_b3": "BBAS3",
  "cod_y": "BBAS3.SA"
 },
 {
  "cod_b3": "ROMI3",
  "cod_y": "ROMI3.SA"
 },
 {
  "cod_b3": "CURY3",
  "cod_y": "CURY3.SA"
 },
 {
  "cod_b3": "JBSS3",
  "cod_y": "JBSS3.SA"
 },
 {
  "cod_b3": "BBSE3",
  "cod_y": "BBSE3.SA"
 },
 {
  "cod_b3": "SAPR11",
  "cod_y": "SAPR11.SA"
 },
 {
  "cod_b3": "DEXP4",
  "cod_y": "DEXP4.SA"
 },
 {
  "cod_b3": "SAPR4",
  "cod_y": "SAPR4.SA"
 },
 {
  "cod_b3": "BRGE11",
  "cod_y": "BRGE11.SA"
 },
 {
  "cod_b3": "CSNA3",
  "cod_y": "CSNA3.SA"
 },
 {
  "cod_b3": "BMKS3",
  "cod_y": "BMKS3.SA"
 },
 {
  "cod_b3": "SAPR3",
  "cod_y": "SAPR3.SA"
 },
 {
  "cod_b3": "COCE5",
  "cod_y": "COCE5.SA"
 },
 {
  "cod_b3": "TRPL4",
  "cod_y": "TRPL4.SA"
 },
 {
  "cod_b3": "PSSA3",
  "cod_y": "PSSA3.SA"
 },
 {
  "cod_b3": "JSLG3",
  "cod_y": "JSLG3.SA"
 },
 {
  "cod_b3": "HBOR3",
  "cod_y": "HBOR3.SA"
 },
 {
  "cod_b3": "BEEF3",
  "cod_y": "BEEF3.SA"
 },
 {
  "cod_b3": "CRPG3",
  "cod_y": "CRPG3.SA"
 },
 {
  "cod_b3": "BGIP4",
  "cod_y": "BGIP4.SA"
 },
 {
  "cod_b3": "BMIN4",
  "cod_y": "BMIN4.SA"
 },
 {
  "cod_b3": "CXSE3",
  "cod_y": "CXSE3.SA"
 },
 {
  "cod_b3": "DEXP3",
  "cod_y": "DEXP3.SA"
 },
 {
  "cod_b3": "ITSA4",
  "cod_y": "ITSA4.SA"
 },
 {
  "cod_b3": "ABCB4",
  "cod_y": "ABCB4.SA"
 },
 {
  "cod_b3": "ITSA3",
  "cod_y": "ITSA3.SA"
 },
 {
  "cod_b3": "KEPL3",
  "cod_y": "KEPL3.SA"
 },
 {
  "cod_b3": "PLPL3",
  "cod_y": "PLPL3.SA"
 },
 {
  "cod_b3": "GRND3",
  "cod_y": "GRND3.SA"
 },
 {
  "cod_b3": "SIMH3",
  "cod_y": "SIMH3.SA"
 },
 {
  "cod_b3": "MTRE3",
  "cod_y": "MTRE3.SA"
 },
 {
  "cod_b3": "B3SA3",
  "cod_y": "B3SA3.SA"
 },
 {
  "cod_b3": "CARD3",
  "cod_y": "CARD3.SA"
 },
 {
  "cod_b3": "FESA4",
  "cod_y": "FESA4.SA"
 },
 {
  "cod_b3": "MERC4",
  "cod_y": "MERC4.SA"
 },
 {
  "cod_b3": "BRSR5",
  "cod_y": "BRSR5.SA"
 },
 {
  "cod_b3": "GUAR3",
  "cod_y": "GUAR3.SA"
 },
 {
  "cod_b3": "EGIE3",
  "cod_y": "EGIE3.SA"
 },
 {
  "cod_b3": "PATI4",
  "cod_y": "PATI4.SA"
 },
 {
  "cod_b3": "WLMM3",
  "cod_y": "WLMM3.SA"
 },
 {
  "cod_b3": "FESA3",
  "cod_y": "FESA3.SA"
 },
 {
  "cod_b3": "TGMA3",
  "cod_y": "TGMA3.SA"
 },
 {
  "cod_b3": "USIM6",
  "cod_y": "USIM6.SA"
 },
 {
  "cod_b3": "EMAE3",
  "cod_y": "EMAE3.SA"
 },
 {
  "cod_b3": "MTSA4",
  "cod_y": "MTSA4.SA"
 },
 {
  "cod_b3": "COCE3",
  "cod_y": "COCE3.SA"
 },
 {
  "cod_b3": "SLCE3",
  "cod_y": "SLCE3.SA"
 },
 {
  "cod_b3": "PORT3",
  "cod_y": "PORT3.SA"
 },
 {
  "cod_b3": "ENGI3",
  "cod_y": "ENGI3.SA"
 },
 {
  "cod_b3": "CSMG3",
  "cod_y": "CSMG3.SA"
 },
 {
  "cod_b3": "NEOE3",
  "cod_y": "NEOE3.SA"
 },
 {
  "cod_b3": "FLRY3",
  "cod_y": "FLRY3.SA"
 },
 {
  "cod_b3": "BSLI3",
  "cod_y": "BSLI3.SA"
 },
 {
  "cod_b3": "EQPA3",
  "cod_y": "EQPA3.SA"
 },
 {
  "cod_b3": "PATI3",
  "cod_y": "PATI3.SA"
 },
 {
  "cod_b3": "TRPL3",
  "cod_y": "TRPL3.SA"
 },
 {
  "cod_b3": "MODL11",
  "cod_y": "MODL11.SA"
 },
 {
  "cod_b3": "JHSF3",
  "cod_y": "JHSF3.SA"
 },
 {
  "cod_b3": "MDIA3",
  "cod_y": "MDIA3.SA"
 },
 {
  "cod_b3": "JALL3",
  "cod_y": "JALL3.SA"
 },
 {
  "cod_b3": "MODL4",
  "cod_y": "MODL4.SA"
 },
 {
  "cod_b3": "TRIS3",
  "cod_y": "TRIS3.SA"
 },
 {
  "cod_b3": "MODL3",
  "cod_y": "MODL3.SA"
 },
 {
  "cod_b3": "HBTS5",
  "cod_y": "HBTS5.SA"
 },
 {
  "cod_b3": "AFLT3",
  "cod_y": "AFLT3.SA"
 },
 {
  "cod_b3": "ALUP11",
  "cod_y": "ALUP11.SA"
 },
 {
  "cod_b3": "ALUP3",
  "cod_y": "ALUP3.SA"
 },
 {
  "cod_b3": "LIGT3",
  "cod_y": "LIGT3.SA"
 },
 {
  "cod_b3": "ALUP4",
  "cod_y": "ALUP4.SA"
 },
 {
  "cod_b3": "CIEL3",
  "cod_y": "CIEL3.SA"
 },
 {
  "cod_b3": "UGPA3",
  "cod_y": "UGPA3.SA"
 },
 {
  "cod_b3": "CSAN3",
  "cod_y": "CSAN3.SA"
 },
 {
  "cod_b3": "AMER3",
  "cod_y": "AMER3.SA"
 },
 {
  "cod_b3": "RDOR3",
  "cod_y": "RDOR3.SA"
 },
 {
  "cod_b3": "EQPA5",
  "cod_y": "EQPA5.SA"
 },
 {
  "cod_b3": "DOHL4",
  "cod_y": "DOHL4.SA"
 },
 {
  "cod_b3": "ESPA3",
  "cod_y": "ESPA3.SA"
 },
 {
  "cod_b3": "EQPA7",
  "cod_y": "EQPA7.SA"
 },
 {
  "cod_b3": "TIMS3",
  "cod_y": "TIMS3.SA"
 },
 {
  "cod_b3": "ABEV3",
  "cod_y": "ABEV3.SA"
 },
 {
  "cod_b3": "EMAE4",
  "cod_y": "EMAE4.SA"
 },
 {
  "cod_b3": "SHUL4",
  "cod_y": "SHUL4.SA"
 },
 {
  "cod_b3": "BBDC3",
  "cod_y": "BBDC3.SA"
 },
 {
  "cod_b3": "FIQE3",
  "cod_y": "FIQE3.SA"
 },
 {
  "cod_b3": "ENMT3",
  "cod_y": "ENMT3.SA"
 },
 {
  "cod_b3": "ENMT4",
  "cod_y": "ENMT4.SA"
 },
 {
  "cod_b3": "CAML3",
  "cod_y": "CAML3.SA"
 },
 {
  "cod_b3": "BRGE5",
  "cod_y": "BRGE5.SA"
 },
 {
  "cod_b3": "CYRE3",
  "cod_y": "CYRE3.SA"
 },
 {
  "cod_b3": "BRGE8",
  "cod_y": "BRGE8.SA"
 },
 {
  "cod_b3": "CPLE5",
  "cod_y": "CPLE5.SA"
 },
 {
  "cod_b3": "UCAS3",
  "cod_y": "UCAS3.SA"
 },
 {
  "cod_b3": "ITUB3",
  "cod_y": "ITUB3.SA"
 },
 {
  "cod_b3": "ELET5",
  "cod_y": "ELET5.SA"
 },
 {
  "cod_b3": "BBDC4",
  "cod_y": "BBDC4.SA"
 },
 {
  "cod_b3": "ELET6",
  "cod_y": "ELET6.SA"
 },
 {
  "cod_b3": "EZTC3",
  "cod_y": "EZTC3.SA"
 },
 {
  "cod_b3": "STBP3",
  "cod_y": "STBP3.SA"
 },
 {
  "cod_b3": "CEPE3",
  "cod_y": "CEPE3.SA"
 },
 {
  "cod_b3": "EUCA4",
  "cod_y": "EUCA4.SA"
 },
 {
  "cod_b3": "PTNT4",
  "cod_y": "PTNT4.SA"
 },
 {
  "cod_b3": "DIRR3",
  "cod_y": "DIRR3.SA"
 },
 {
  "cod_b3": "BGIP3",
  "cod_y": "BGIP3.SA"
 },
 {
  "cod_b3": "JOPA3",
  "cod_y": "JOPA3.SA"
 },
 {
  "cod_b3": "LOGG3",
  "cod_y": "LOGG3.SA"
 },
 {
  "cod_b3": "MRVE3",
  "cod_y": "MRVE3.SA"
 },
 {
  "cod_b3": "TECN3",
  "cod_y": "TECN3.SA"
 },
 {
  "cod_b3": "BPAN4",
  "cod_y": "BPAN4.SA"
 },
 {
  "cod_b3": "VBBR3",
  "cod_y": "VBBR3.SA"
 },
 {
  "cod_b3": "MULT3",
  "cod_y": "MULT3.SA"
 },
 {
  "cod_b3": "POSI3",
  "cod_y": "POSI3.SA"
 },
 {
  "cod_b3": "BPAC5",
  "cod_y": "BPAC5.SA"
 },
 {
  "cod_b3": "ITUB4",
  "cod_y": "ITUB4.SA"
 },
 {
  "cod_b3": "SUZB3",
  "cod_y": "SUZB3.SA"
 },
 {
  "cod_b3": "ODPV3",
  "cod_y": "ODPV3.SA"
 },
 {
  "cod_b3": "BMEB4",
  "cod_y": "BMEB4.SA"
 },
 {
  "cod_b3": "BRKM6",
  "cod_y": "BRKM6.SA"
 },
 {
  "cod_b3": "HYPE3",
  "cod_y": "HYPE3.SA"
 },
 {
  "cod_b3": "CSED3",
  "cod_y": "CSED3.SA"
 },
 {
  "cod_b3": "CRFB3",
  "cod_y": "CRFB3.SA"
 },
 {
  "cod_b3": "QUAL3",
  "cod_y": "QUAL3.SA"
 },
 {
  "cod_b3": "VLID3",
  "cod_y": "VLID3.SA"
 },
 {
  "cod_b3": "MTSA3",
  "cod_y": "MTSA3.SA"
 },
 {
  "cod_b3": "MILS3",
  "cod_y": "MILS3.SA"
 },
 {
  "cod_b3": "EQPA6",
  "cod_y": "EQPA6.SA"
 },
 {
  "cod_b3": "RSUL4",
  "cod_y": "RSUL4.SA"
 },
 {
  "cod_b3": "ATOM3",
  "cod_y": "ATOM3.SA"
 },
 {
  "cod_b3": "LIPR3",
  "cod_y": "LIPR3.SA"
 },
 {
  "cod_b3": "JOPA4",
  "cod_y": "JOPA4.SA"
 },
 {
  "cod_b3": "MLAS3",
  "cod_y": "MLAS3.SA"
 },
 {
  "cod_b3": "EQTL3",
  "cod_y": "EQTL3.SA"
 },
 {
  "cod_b3": "MRSA6B",
  "cod_y": "MRSA6B.SA"
 },
 {
  "cod_b3": "LPSB3",
  "cod_y": "LPSB3.SA"
 },
 {
  "cod_b3": "PARD3",
  "cod_y": "PARD3.SA"
 },
 {
  "cod_b3": "OFSA3",
  "cod_y": "OFSA3.SA"
 },
 {
  "cod_b3": "VULC3",
  "cod_y": "VULC3.SA"
 },
 {
  "cod_b3": "WLMM4",
  "cod_y": "WLMM4.SA"
 },
 {
  "cod_b3": "BALM4",
  "cod_y": "BALM4.SA"
 },
 {
  "cod_b3": "VVEO3",
  "cod_y": "VVEO3.SA"
 },
 {
  "cod_b3": "MRSA3B",
  "cod_y": "MRSA3B.SA"
 },
 {
  "cod_b3": "AGXY3",
  "cod_y": "AGXY3.SA"
 },
 {
  "cod_b3": "FRAS3",
  "cod_y": "FRAS3.SA"
 },
 {
  "cod_b3": "CBEE3",
  "cod_y": "CBEE3.SA"
 },
 {
  "cod_b3": "BMEB3",
  "cod_y": "BMEB3.SA"
 },
 {
  "cod_b3": "CSAB4",
  "cod_y": "CSAB4.SA"
 },
 {
  "cod_b3": "BLAU3",
  "cod_y": "BLAU3.SA"
 },
 {
  "cod_b3": "LVTC3",
  "cod_y": "LVTC3.SA"
 },
 {
  "cod_b3": "ALPA3",
  "cod_y": "ALPA3.SA"
 },
 {
  "cod_b3": "CBAV3",
  "cod_y": "CBAV3.SA"
 },
 {
  "cod_b3": "LREN3",
  "cod_y": "LREN3.SA"
 },
 {
  "cod_b3": "ALSO3",
  "cod_y": "ALSO3.SA"
 },
 {
  "cod_b3": "MRSA5B",
  "cod_y": "MRSA5B.SA"
 },
 {
  "cod_b3": "BALM3",
  "cod_y": "BALM3.SA"
 },
 {
  "cod_b3": "ALPA4",
  "cod_y": "ALPA4.SA"
 },
 {
  "cod_b3": "SEER3",
  "cod_y": "SEER3.SA"
 },
 {
  "cod_b3": "BPAC11",
  "cod_y": "BPAC11.SA"
 },
 {
  "cod_b3": "CSAB3",
  "cod_y": "CSAB3.SA"
 },
 {
  "cod_b3": "EUCA3",
  "cod_y": "EUCA3.SA"
 },
 {
  "cod_b3": "IGTI3",
  "cod_y": "IGTI3.SA"
 },
 {
  "cod_b3": "VITT3",
  "cod_y": "VITT3.SA"
 },
 {
  "cod_b3": "LJQQ3",
  "cod_y": "LJQQ3.SA"
 },
 {
  "cod_b3": "SBSP3",
  "cod_y": "SBSP3.SA"
 },
 {
  "cod_b3": "ARZZ3",
  "cod_y": "ARZZ3.SA"
 },
 {
  "cod_b3": "CEGR3",
  "cod_y": "CEGR3.SA"
 },
 {
  "cod_b3": "ELET3",
  "cod_y": "ELET3.SA"
 },
 {
  "cod_b3": "POMO3",
  "cod_y": "POMO3.SA"
 },
 {
  "cod_b3": "IGTI11",
  "cod_y": "IGTI11.SA"
 },
 {
  "cod_b3": "ARML3",
  "cod_y": "ARML3.SA"
 },
 {
  "cod_b3": "PRNR3",
  "cod_y": "PRNR3.SA"
 },
 {
  "cod_b3": "PTNT3",
  "cod_y": "PTNT3.SA"
 },
 {
  "cod_b3": "PCAR3",
  "cod_y": "PCAR3.SA"
 },
 {
  "cod_b3": "PNVL3",
  "cod_y": "PNVL3.SA"
 },
 {
  "cod_b3": "CAMB3",
  "cod_y": "CAMB3.SA"
 },
 {
  "cod_b3": "WEGE3",
  "cod_y": "WEGE3.SA"
 },
 {
  "cod_b3": "RAIZ4",
  "cod_y": "RAIZ4.SA"
 },
 {
  "cod_b3": "TPIS3",
  "cod_y": "TPIS3.SA"
 },
 {
  "cod_b3": "POMO4",
  "cod_y": "POMO4.SA"
 },
 {
  "cod_b3": "BMOB3",
  "cod_y": "BMOB3.SA"
 },
 {
  "cod_b3": "DASA3",
  "cod_y": "DASA3.SA"
 },
 {
  "cod_b3": "GGPS3",
  "cod_y": "GGPS3.SA"
 },
 {
  "cod_b3": "VAMO3",
  "cod_y": "VAMO3.SA"
 },
 {
  "cod_b3": "RENT3",
  "cod_y": "RENT3.SA"
 },
 {
  "cod_b3": "CAMB4",
  "cod_y": "CAMB4.SA"
 },
 {
  "cod_b3": "INTB3",
  "cod_y": "INTB3.SA"
 },
 {
  "cod_b3": "BRPR3",
  "cod_y": "BRPR3.SA"
 },
 {
  "cod_b3": "VIVA3",
  "cod_y": "VIVA3.SA"
 },
 {
  "cod_b3": "BPAC3",
  "cod_y": "BPAC3.SA"
 },
 {
  "cod_b3": "CCRO3",
  "cod_y": "CCRO3.SA"
 },
 {
  "cod_b3": "EVEN3",
  "cod_y": "EVEN3.SA"
 },
 {
  "cod_b3": "TFCO4",
  "cod_y": "TFCO4.SA"
 },
 {
  "cod_b3": "RADL3",
  "cod_y": "RADL3.SA"
 },
 {
  "cod_b3": "DOHL3",
  "cod_y": "DOHL3.SA"
 },
 {
  "cod_b3": "AESB3",
  "cod_y": "AESB3.SA"
 },
 {
  "cod_b3": "AMBP3",
  "cod_y": "AMBP3.SA"
 },
 {
  "cod_b3": "TUPY3",
  "cod_y": "TUPY3.SA"
 },
 {
  "cod_b3": "YDUQ3",
  "cod_y": "YDUQ3.SA"
 },
 {
  "cod_b3": "BOAS3",
  "cod_y": "BOAS3.SA"
 },
 {
  "cod_b3": "BRIV3",
  "cod_y": "BRIV3.SA"
 },
 {
  "cod_b3": "MATD3",
  "cod_y": "MATD3.SA"
 },
 {
  "cod_b3": "AERI3",
  "cod_y": "AERI3.SA"
 },
 {
  "cod_b3": "SULA4",
  "cod_y": "SULA4.SA"
 },
 {
  "cod_b3": "SULA11",
  "cod_y": "SULA11.SA"
 },
 {
  "cod_b3": "SULA3",
  "cod_y": "SULA3.SA"
 },
 {
  "cod_b3": "NTCO3",
  "cod_y": "NTCO3.SA"
 },
 {
  "cod_b3": "ASAI3",
  "cod_y": "ASAI3.SA"
 },
 {
  "cod_b3": "LUXM4",
  "cod_y": "LUXM4.SA"
 },
 {
  "cod_b3": "NGRD3",
  "cod_y": "NGRD3.SA"
 },
 {
  "cod_b3": "RDNI3",
  "cod_y": "RDNI3.SA"
 },
 {
  "cod_b3": "TOTS3",
  "cod_y": "TOTS3.SA"
 },
 {
  "cod_b3": "LAND3",
  "cod_y": "LAND3.SA"
 },
 {
  "cod_b3": "SOMA3",
  "cod_y": "SOMA3.SA"
 },
 {
  "cod_b3": "AURE3",
  "cod_y": "AURE3.SA"
 },
 {
  "cod_b3": "BRML3",
  "cod_y": "BRML3.SA"
 },
 {
  "cod_b3": "SCAR3",
  "cod_y": "SCAR3.SA"
 },
 {
  "cod_b3": "RECV3",
  "cod_y": "RECV3.SA"
 },
 {
  "cod_b3": "PETZ3",
  "cod_y": "PETZ3.SA"
 },
 {
  "cod_b3": "SBFG3",
  "cod_y": "SBFG3.SA"
 },
 {
  "cod_b3": "CASN4",
  "cod_y": "CASN4.SA"
 },
 {
  "cod_b3": "SQIA3",
  "cod_y": "SQIA3.SA"
 },
 {
  "cod_b3": "SOJA3",
  "cod_y": "SOJA3.SA"
 },
 {
  "cod_b3": "APER3",
  "cod_y": "APER3.SA"
 },
 {
  "cod_b3": "CASN3",
  "cod_y": "CASN3.SA"
 },
 {
  "cod_b3": "HAPV3",
  "cod_y": "HAPV3.SA"
 },
 {
  "cod_b3": "FIGE3",
  "cod_y": "FIGE3.SA"
 },
 {
  "cod_b3": "ODER4",
  "cod_y": "ODER4.SA"
 },
 {
  "cod_b3": "SHUL3",
  "cod_y": "SHUL3.SA"
 },
 {
  "cod_b3": "TTEN3",
  "cod_y": "TTEN3.SA"
 },
 {
  "cod_b3": "DESK3",
  "cod_y": "DESK3.SA"
 },
 {
  "cod_b3": "RAIL3",
  "cod_y": "RAIL3.SA"
 },
 {
  "cod_b3": "BRIT3",
  "cod_y": "BRIT3.SA"
 },
 {
  "cod_b3": "RPAD6",
  "cod_y": "RPAD6.SA"
 },
 {
  "cod_b3": "RPAD3",
  "cod_y": "RPAD3.SA"
 },
 {
  "cod_b3": "TRAD3",
  "cod_y": "TRAD3.SA"
 }
]

dat = []

teste = pd.DataFrame(dat)
for dado in cods:

    acao = yf.Ticker(dado['cod_y'])

    acao = acao.dividends

    acao = pd.DataFrame(acao)

    acao["data"] = acao.index
    acao['Cod'] = dado['cod_b3']
    acao['id'] = 0
    acao.set_index('id')
    novo = acao.values.tolist()

    teste.append(acao)
    dat.append(novo)


now_dividendos = []

for dado in dat:
    # new_dividendos.append()
    for inf in dado:
        print(type(inf[0]),type(inf[1]),type(inf[2]))##dado[1], dado[3])
        now_dividendos.append({"cod": inf[2],"data": inf[1], "dividendo": inf[0]})

now_dividendos = pd.DataFrame(now_dividendos)

now_dividendos.to_excel("divid.xlsx")

