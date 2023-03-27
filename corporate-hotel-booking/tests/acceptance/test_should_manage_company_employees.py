from src.company.company_service import CompanyService

COMPANY_ID = '3ade019b-c718-4ebc-89ff-ddc9512c96f0'
EMPLOYEE_ID = 'ae5c0343-70ec-40af-811d-94867bf1ae1b'


def test_should_be_able_to_delete_employee(employee_repository):
    company_service = CompanyService(employee_repository=employee_repository)
    company_service.add_employee(company_id=COMPANY_ID, employee_id=EMPLOYEE_ID)
    company_service.delete_employee(employee_id=EMPLOYEE_ID)
