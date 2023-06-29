package com.github.ambersariya.booking;

import com.github.ambersariya.core.CompanyId;

public interface BookingPolicyRepository {
    void save(CompanyPolicy companyPolicy);
    void save(EmployeePolicy employeePolicy);
    CompanyPolicy findCompanyPolicyBy(CompanyId companyId);
    EmployeePolicy findEmployeePolicyBy(int employeeId);
}
