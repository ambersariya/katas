package com.github.ambersariya.booking;

public interface BookingPolicyRepository {
    void save(CompanyPolicy companyPolicy);
    void save(EmployeePolicy employeePolicy);
    CompanyPolicy findCompanyPolicyBy(int companyId);
    EmployeePolicy findEmployeePolicyBy(int employeeId);
}
