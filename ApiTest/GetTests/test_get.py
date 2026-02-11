# import requests
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from Infra.BaseData.GetData import VarData, loaded_data, get_headers

# class PageOutputDTO:
#     def __init__(self, page):
#         self.result = {"page": page}
#     def to_json(self):
#         return self.data

# def test_baba():
#     url = loaded_data[VarData.BaseApiUrl] +"users?page=2"
#     headers = get_headers()
#     response = requests.get(url, headers=headers)
#     assert response.status_code == 200

#     response_data = response.json()
#     output_dto = PageOutputDTO(response_data['page'])
#    # assert output_dto.result['page']==2



