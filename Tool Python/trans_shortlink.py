#library

import requests

#data

ck='lang=eyJpdiI6ImxmRVpFQ29jbUlsRkd5YTE3TVNibWc9PSIsInZhbHVlIjoidDUvd0RjVFlUbkxrNTkrbUJkNnErWWNzYjdUc1htUGViMGJUQjBoYWs0SGE1dXR6bkczNkt5REJCS2VDSjJObiIsIm1hYyI6ImRmNmMyMGU5ODUxOTZhODBiY2JmZTMxNzllM2VjMGM3ZGVkZjk2MjQ0NmI1ZjdlNWU4MjQ0ZmRmYjM3NzE0OWUifQ%3D%3D; _ga=GA1.1.1142560212.1696414605; csaas_user_id=0.x48u32oghk9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InlMVS9sdTN3bmRzNGYveVJpUmRBQXc9PSIsInZhbHVlIjoicmx1YWVGYnozblBjMnp0WFBKNGxiZW5wOWd3OUMyRFNuYi90WWhMODRwSEVtRVF5d3BQWmozdGh3Nkw2TzBEWEtJR1ByM04zSE4vRkhhVjRUYndQNkRVSXd1WXBBOE91VzJXRnFkNllRL0NTMmI1VUxTOTgxMWhzK1c4bEFrQ0NyUHZLY2xoU0k5bHlJcVFPbWJUVEhRU0NGdnRvbFhGdWhkdkwrZVhTMVpkcmg0Uy93SENGK2ljR2tOb3dQLzYrL1AzVThlK0xFNFY4NHl6bk5QWGI3bjJ1T0tuQ2tMQlFvN2dMTG9XNmdCVT0iLCJtYWMiOiJlYmNlMGRmNTlhMjIzNzhlYmI0MTQ3MzcwN2Y1ZGZhNDI2NjZiNGU1NmUwNTdmYjQ0YTU2ZGE2OWEyZTYyOTg5In0%3D; cf_clearance=z_fSTEdns9cpPqGIP77byXBohqHnuZ.4JQBW4qW8IsA-1700527864-0-1-5addf350.23721535.ddcacb0-250.0.0; triggeredForPjlHFsfb=ia8mhd2xti; _ga_FFP7FJ85WV=GS1.1.1702696094.21.0.1702696095.0.0.0; web1s_session=2DiKvj9itT7V8Gl5L0fyhUN6DDJBCLhHn5V865ba; csaas_referrer=; cSaasWidget_ia8mhd2xti=[{"k":"v-widget","v":"2023-12-20T23:39:20.928Z"}]; activeCsaasWidgets=ia8mhd2xti; XSRF-TOKEN=eyJpdiI6Ind4SStyS0phNmdBVnJ2Rk1WWGdWbXc9PSIsInZhbHVlIjoiUlYzNExqMDk1RHRYTXAva05wOGlXTW1RUjFCbytoVDRoYkxRR2NFcWVUWmdaanVHdEtaOEVQS2tvbkUxOTFrVmVtVE1BWGxheXlRak5aSUs4L0RTaU5hRjNYb0dPRDhuN0Vwc3FjMTZ1andGR1hPYm0zUzlQbkx6bzZXSEJaL2giLCJtYWMiOiI1ZDBlZWUwZjcwZTVmMmQyMGZlMzY0N2YwNThkYWY5YTdiYTdlOThkODU5OTVkZDI4ODViMTc5YTNlMjFiM2YxIn0%3D; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjAuMC4wLjA%3D; '

token="eyJpdiI6IklLcUtGMDJQclBEdXRGSklGdUF3SkE9PSIsInZhbHVlIjoibFA3T3NvNU9yYzJ4LzJ6QWltaGNnV29IQ2N6b0p4VFZzRkF2MXlLNTkrREtjM2lBRkpFa2N0U1F1QWNiZFVaN2JGYjRaOG1CSnR0Z2UyelNSV1dacGNPUldheGlNbE5TdlRQQlBhUTUxbWRIMWM3N0dMYjdGSFVrR0lkVForajIiLCJtYWMiOiIzODUzZDI2YjFmODQ4ZGQ2Y2VhMmQ5Yzg0Yjk0MzEzZDc3NDZlMWFkMDhiYzc5Mjg0NWY0MmQyNDE4MjRjZGQ4In0="

while True:

    link_found=input("Type a link: ")

    #code

    head_web1s={
        'host':'web1s.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
        'cookie':ck,

    }

    data_web1s=f'alias=&level_id=0&token_id=0&source=0&search={link_found}&page=1&per_page=20&order_field=&order_type=asc&is_hidden=0'

    require=requests.get(f'https://web1s.com/member/api/links?alias=&level_id=0&token_id=0&source=0&search={link_found}&page=1&per_page=20&order_field=&order_type=asc&is_hidden=0',data=data_web1s,headers=head_web1s).json()

    link_key=require['data'][0]['url']

    print(link_key)


    def short_link(link_key):
        api_token = '63a469a81f362c35c12f2d80'
        api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={link_key}"
        result = requests.get(api_url).json()
        if result['status'] == 'error':
            print(result['message'])
        else:
            print(f"Link get key => {result['shortenedUrl']} ")


    short_link(link_key)






