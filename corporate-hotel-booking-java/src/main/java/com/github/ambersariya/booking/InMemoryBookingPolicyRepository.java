package com.github.ambersariya.booking;

import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;

import java.util.HashMap;

public class InMemoryBookingPolicyRepository implements BookingPolicyRepository {
    private final HashMap<CompanyId, CompanyPolicy> companyPolicies = new HashMap<>();
    private final HashMap<EmployeeId, EmployeePolicy> employeePolicies = new HashMap<EmployeeId, EmployeePolicy>();
    @Override
    public void save(CompanyPolicy companyPolicy) {
        companyPolicies.put(companyPolicy.companyId(), companyPolicy);
    }

    @Override
    public void save(EmployeePolicy employeePolicy) {
        employeePolicies.put(employeePolicy.employeeId(), employeePolicy);
    }

    @Override
    public CompanyPolicy findCompanyPolicyBy(CompanyId companyId) {
        return companyPolicies.get(companyId);
    }

    @Override
    public EmployeePolicy findEmployeePolicyBy(EmployeeId employeeId) {
        return employeePolicies.get(employeeId);
    }

}
