from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from signup_api.serializers.company_serializer import CompanySerializer
from signup_api.serializers.company_vo import CompanyVo
from signup_api.serializers.create_one_company_dto_serializer import (
    CreateOneCompanyDtoSerializer,
)
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


CREATE_COMPANY_SUCCESS = """
{
    "status": "success",
    "data": {
        "company": {
                "id": "xxx",
                "companyName":"xxx",
                "email":"xxx"
        }
    }
}
"""

CREATE_COMPANY_FAILURE = """
{
    "status": "error",
    "message": "error message"
}
"""


# Create your views here.
class Companies(APIView):
    @swagger_auto_schema(
        request_body=CreateOneCompanyDtoSerializer,
        responses={200: CREATE_COMPANY_SUCCESS, 400: CREATE_COMPANY_FAILURE},
    )
    def post(self, request: Request):
        create_company_dto_serializer = CreateOneCompanyDtoSerializer(data=request.data)
        if create_company_dto_serializer.is_valid():
            create_company_dto = create_company_dto_serializer.data
            company_serializer = CompanySerializer(
                data={
                    "company_name": create_company_dto["companyName"],
                    **create_company_dto,
                }
            )
            if company_serializer.is_valid():
                company_serializer.save()
                new_company_do = company_serializer.data
                company_vo = CompanyVo(
                    id=new_company_do["id"],
                    companyName=new_company_do["company_name"],
                    email=new_company_do["email"],
                )

                return Response(
                    {
                        "status": "success",
                        "data": {"company": company_vo},
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": "error",
                        "message": company_serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"status": "error", "message": create_company_dto_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
