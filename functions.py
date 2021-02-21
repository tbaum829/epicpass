import sched
import time
import requests
from pygame import mixer

resorts = {
    "Breckenridge": 3,
    "Keystone": 4
}

cookie = "_fbp=fb.1.1612150640394.1941926284; s_invisit=true; s_lv=1612490226129; s_lv_s=Less%20than%201%20day; " \
         "s_nr=1612490226130-Repeat; s_sq=vriepicpass%252Cvailglobal%3D%2526c.%2526a.%2526activitymap.%2526page" \
         "%253DEpic%252520Pass%25253Aplan-your-trip%25253Alift-access%25253AReservations%2526link%253DCHECK" \
         "%252520AVAILABILITY%2526region%253DpassHolderReservations__wrapper%2526pageIDType%253D1%2526.activitymap" \
         "%2526.a%2526.c%2526pid%253DEpic%252520Pass%25253Aplan-your-trip%25253Alift-access%25253AReservations" \
         "%2526pidt%253D1%2526oid%253DfunctionBe%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; " \
         "s_vnum=1613161420503%26vn%3D4; " \
         "dtCookie=v_4_srv_3_sn_B12DFB07976EBA6979044C72D5A778CF_perc_100000_ol_0_mul_1_app-3A0d20c77a5fc281dd_0; " \
         "rxVisitor=161249013919826CUUJGJ5BVJIRPCHIL9QNNDIFVM0MS8; LPSID-31842070=X4Q2jToETyCtUZ_ms9DZEw; " \
         "LPVID=UxYTY3YmI1NmUxNzFkYTAw; " \
         "bm_sv=55A37E027944EECA96EA5603815DEEAD~hc7H91eiUNWHuOs6MWkMUS9x0eewVMwyPtbLot2We6I" \
         "/BH2eVguWAshlh9kIBPbMSCHIqYn6cVtRvMkBKS1CFTfKr7oOeQOfPHG+ywAU9ptlds3YpcDC4SbMoMGPao7uzAgAfuYD3O9gxJ" \
         "/z3895A8bfNI0DqQgw/5LubMtakFI=; s_ppv=Epic%2520Pass%253Aplan-your-trip%253Alift-access%253AReservations" \
         "%2C70%2C13%2C1185; AAMC_vailresorts_0=REGION%7C9; aam_uuid=67214413933888568093475972657517298277; " \
         "adcloud={%22_les_v%22:%22y%2Cepicpass.com%2C1612492013%22}; " \
         "dtPC=3$290212189_43h-vECWUSFHMBMMTRHCMKLERVBOJHFSKFPHC-0e6; " \
         "gpv_pn=Epic%20Pass%3Aplan-your-trip%3Alift-access%3AReservations; " \
         "rbuid=rbos-b7a5dab3-2a48-40dd-a2bc-273471df1a16; rxvt=1612492013060|1612490139200; s_cc=true; s_tp=1700; " \
         "RT=\"z=1&dm=www.epicpass.com&si=5af27c8b-8290-4bc3-afcd-70b8bcba7bd9&ss=kkrmzth8&sl=6&tt=c1i&bcn=%2F" \
         "%2F173e250d.akstat.io%2F&ld=1lu4\"; " \
         "AMCV_974C370453295F9A0A490D44%40AdobeOrg=1406116232%7CMCIDTS%7C18664%7CMCMID" \
         "%7C59835243926603887754500158539883277355%7CMCAID%7CNONE%7CMCOPTOUT-1612497339s%7CNONE%7CMCAAMLH-1613095013" \
         "%7C9%7CMCAAMB-1613095013%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18667%7CMCCIDH" \
         "%7C-556352570%7CvVersion%7C2.5.0; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+04+2021+18%3A56%3A52" \
         "+GMT-0700+(MST)&version=5.13.0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004" \
         "%3A1&hosts=&AwaitingReconsent=false&geolocation=%3B; " \
         "TS01746597" \
         "=01d73c084b82fa01027f6efa3523921c549df7435109d8bd2fe4a348a14c949fb4ba069b732525c9ed5a12455263201001e62bd233" \
         "; check=true; dtSa=-; mbox=PC#33ef2889f56e43e081bace3edb2ac79b.35_0#1675395439|session" \
         "#edebe6714f5f4a78ac119996ad9c1648#1612492073; vr_product_reminder=true; " \
         "QueueITAccepted-SDFrts345E-V3_epicpasspriority1203=EventId%3Depicpasspriority1203%26QueueId%3D545ebab1-9df3" \
         "-421f-bcb1-ad8c12b6fb94%26RedirectType%3Dsafetynet%26IssueTime%3D1612490222%26Hash" \
         "%3Df1b143dc2fe50ec6c709783108796afe15e0bc06e7fff4aa90e37933bc6b37c7; " \
         "TS019b45a2" \
         "=01d73c084b82fa01027f6efa3523921c549df7435109d8bd2fe4a348a14c949fb4ba069b732525c9ed5a12455263201001e62bd233" \
         "; dDrposID=38591570; dDuserEmail=tbaum829@gmail.com; " \
         "vr3_authenticated=95140886-d36b-4db9-92a6-19bba3ac1042; dtLatC=17; " \
         "OptanonAlertBoxClosed=2021-02-05T01:56:10.927Z; " \
         "QueueITAccepted-SDFrts345E-V3_vailresortsecomm1=EventId%3Dvailresortsecomm1%26QueueId%3Db5381f8c-bc04-4d82" \
         "-be1d-1456da76fd54%26RedirectType%3Dsafetynet%26IssueTime%3D1612490163%26Hash" \
         "%3D289d41994597129fdcc9fbfd2b105396d559b744e377b1f1d1d1fffa529af77e; " \
         "vr3_secure_auth=LcMx_7nhxLriBIV1Cgbc6g2=dc4VGfF-2zCylUrv9vxp4g2&fKtZw7qa_sg1=OMROdzhWEENqd-h7EQVCoA2; " \
         ".ASPXAUTH" \
         "=42E5B13D124968B70CAAA0FF317EA8FEE481B5047005341AA519335F0BE0E56A2CF285D4084E5A222BCB7623F2257DCDE9880410596DAE85310D63F43C636F35A6330B3972330E4A13C170BCC65331494E23DC22378367EC95D66908D41E526079C22EA484C9C066407A1907D7662F58F6F34CBAE191633B303617A364568CF12B5EAF421FC103992BAAC2C6C3A1EA7E23AF164278FF2E8D0440D3EC1695ABFC934491D72D2989E71E16D9853AA392800A07D00EED6F053D6D1BABB97437C42CD59F29E6311FBF765B37190029550E0946293857A337177D5631DC244C0D608A7A569C959B7D1FC9F5A0B68FE612DEB93F16123E0A98313265AEBAE119D40EF2CBAB86DDC6CBE02B6F5B8E5C2C0E171D745F25A049997D30EB8B4DAC3554AAFFE4E13D3B7B52840B1882C5CF48F5D05C0FFFC3E972EB4CF6C7F168A5DBCE71C8E16508F0; TS019d4a57=01d73c084b9504e9222c39d95b98c09d2d4ff5f98254f217473344d5cf1cb48c607caed67319da19cf9133e675bfa1225dc9ff3540; __RequestVerificationToken=oEZH1plQjMzVmsZiUJU9vF_Frp3OkrqTOu-fD6yFvSNmAK60F8lPN2UdBVd_VeDLin_TgNd0sQy9tTZYnTlqsDSgMDY1; _abck=4F27937DE3895985F425D5C8712A9806~0~YAAQZg0wFyY2xlt3AQAAMPPmbwV3jiRxGf2QHXluo/wl1ATthmVEgLcam9JSjAviOTJe3brd5thuIytNQH9nxRjO1JJdIpQEM77vPHFdn0Oq69ZZ/J47IzTvEOtN6CttrkWAVtBi2vfePhk3k5atG5AnuUBzo6HBhB39y2tZeLSwagqL1//eOoRtf2kwVCyTmcsfO0OeH5eB9yjqJKZbwE2Boi/dFokKVIUDzDvHL1c6YL+txsttA3YTrKfm8ddp56CmtLdtlsbpIa8lrHqpT+FzT4WlCjShfZBFrNSNDWJKUboRWad6TTWNpyBfyy7mZFeWE0DUrGegJ8DthbRCfmGqMb+gykCn~-1~-1~-1; ak_bmsc=EF1D2361D26263FFF2BB1AFAD31FF03417300D663520000099A51C60B71C5B01~plvGRGnX3Jm16SowZABRH84jvDS0JLDGeLmb01FU3XbOYh0S6WAga+sqfe7gtUsSSCh6S+tHXqfeWwrkzmligULrzgEsfdVD84dbpLceWiyvWSjyOSYSO9ZGLpF+3/Hbj4QUJvPDqrmguxHyoxHpStGA4SWfVpCtHtfOtxYs870bZMQrupCDmrMo9HkmVz4ZqbsARlhQ/xrd4/6zoovpF4BwCO+6PO5Y9p/fxtYz1/lvC3DVuV2F7XuKugb13LGbmy; bm_mi=0CADFC83AEF83FAC378002AA895BB67C~/4QL+6Dmb+/qloz+ZOXI5D9AOL6fL5mCkHw41a+W8k0uXbo4QMc8fGWceoTklrO7Gb30PffTTvFfa+YHjehpbZwlSPj0WStY+chHWxffuho6m5RjxqgEPc5uDznbwiWLXE5VywEvUBstNEjgOeKwkzSdQp2l4jGTlJPCNTp4z+JiDWJzQ8OTrxpNWrOUhXP3R/b0k0/usdRcRD/NZ06YCnvVHOPcm/bMeODO/c89PW0FsVnha1ADwTq9wzAD0hkaZCntEFs9S1bQ4dBv6OSkwQ==; AMCVS_974C370453295F9A0A490D44%40AdobeOrg=1; ASP.NET_SessionId=fzc5nwhuiqlixguusalmi0en; SC_ANALYTICS_GLOBAL_COOKIE=f929d69e6aa94c2c8ca18264c1571c07|False; AKA_A2=A; bm_sz=1715B6BCD8A63CAD194F1CC736B13BB3~YAAQZg0wF+01xlt3AQAAJeDmbwpARe6BEn30Y4g9OAc7quT6nS9IQK/lItrgFDF7dlnHRYd2HLV8+givGDCo/1KhQjol4XQz1j+2cyWx3TF76dfnUjUM8xpm02t9udKNEt6ilWyplrq129hbc4g6U19INtZhZReJe1aGtaDovhdNl4N6HCOi4zTvBi2iEkQT6QM=; dDecID=111776074; _pxvid=c8a88895-643e-11eb-9953-0242ac120011; AMCV_974C370453295F9A0A490D44%40AdobeOrg=T "
token = "ZSe8x99TdSotAlCmk8UWnn9pi9rtu7g35ISauysaKJfIu6iml5967UF-9ZLMW_3MUBuTms73XE-kLSB_3afapvhtOyA1" \
        ":yLJ9imJdmq6Lb047e8IqBI6X67pGToRAVv0OLWaFzSzYiBJJ1zWLXr7HjZubat8PzIeQIpIAxh0q6aNXZOA1nK6gSTiVZpodFu_rTlbud0Pu3Rjo0 "

headers = {
    "Cookie": cookie,
    "__RequestVerificationToken": token,
}
    

def look_for_opening(date, resort):
    s = sched.scheduler(time.time, time.sleep)
    date_string = date.replace('-', '%2F')
    [month, day, year] = date.split('-')
    full_date = '20' + '-'.join([year, month, day]) + 'T00:00:00'
    url = "https://www.epicpass.com/api/LiftAccessApi/GetCapacityControlReservationInventory?resortCode=" + \
          str(resorts[resort]) + "&startDate=" + date_string + "&endDate=" + date_string + "&_=1612490591317"

    def check_availability(sc):
        response = requests.get(url, headers=headers)
        no_inventory_days = response.json()["NoInventoryDays"]
        available = full_date not in no_inventory_days
        print(response.json()["NoInventoryDays"])
        if available:
            mixer.init()  # you must initialize the mixer
            alert = mixer.Sound('baegcdthipc.wav')
            alert.play()
        s.enter(10, 1, check_availability, (sc,))

    s.enter(1, 1, check_availability, (s,))
    s.run()
