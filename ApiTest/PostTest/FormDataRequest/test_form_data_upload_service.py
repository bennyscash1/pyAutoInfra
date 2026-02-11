import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions, HttpCallOptionsSimple, HttpMethod
from ApiTest.PostTest.FormDataRequest.form_dto import FormUploadDTO


def test_form_data_upload_service():
    # Arrange
    svc = HttpService(HttpServiceOptions(base_url="https://httpbin.org"))

    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )

    file_path = os.path.join(BASE_DIR, "Infra", "GeneralFiles", "test.txt")
    assert os.path.exists(file_path), "Test file does not exist"

    call = HttpCallOptionsSimple(path="/post", method=HttpMethod.POST)

    payload = FormUploadDTO(username="benny", role="qa", file_path=file_path)

    # Act
    response_data = svc.call_form_data(
        call,
        data={
            "username": payload.username,
            "role": payload.role,
        },
        files={
            "files": payload.file_path,
        },  # same key as Postman
        return_type="json",
    )

    # Assert – HTTPBIN echo validation
    assert isinstance(response_data, dict)

    form = response_data.get("form")
    files = response_data.get("files")

    assert form["username"] == "benny"
    assert form["role"] == "qa"

    assert "files" in files
    assert files["files"] is not None
