package com.github.ambersariya.booking;

import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;

public interface BookingPolicyRepository {
    void save(CompanyPolicy companyPolicy);
    void save(EmployeePolicy employeePolicy);
    CompanyPolicy findCompanyPolicyBy(CompanyId companyId);
    EmployeePolicy findEmployeePolicyBy(EmployeeId employeeId);
}
