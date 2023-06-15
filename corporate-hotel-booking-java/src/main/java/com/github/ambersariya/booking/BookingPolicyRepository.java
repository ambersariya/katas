package com.github.ambersariya.booking;

public interface BookingPolicyRepository {
    void saveCompanyPolicy(CompanyPolicy companyPolicy);

    void saveEmployeePolicy(EmployeePolicy employeePolicy);

    CompanyPolicy findCompanyPolicyBy(int companyId);

    EmployeePolicy findEmployeePolicyBy(int employeeId);

    int findCompanyIdBy(int employeeId);
}
