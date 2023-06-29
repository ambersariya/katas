package com.github.ambersariya.booking;

import java.util.HashMap;

public class InMemoryBookingPolicyRepository implements BookingPolicyRepository {
    private final HashMap<Integer, CompanyPolicy> companyPolicies = new HashMap<>();
    private final HashMap<Integer, EmployeePolicy> employeePolicies = new HashMap<>();
    @Override
    public void save(CompanyPolicy companyPolicy) {
        companyPolicies.put(companyPolicy.companyId(), companyPolicy);
    }

    @Override
    public void save(EmployeePolicy employeePolicy) {
        employeePolicies.put(employeePolicy.employeeId(), employeePolicy);
    }

    @Override
    public CompanyPolicy findCompanyPolicyBy(int companyId) {
        return companyPolicies.get(companyId);
    }

    @Override
    public EmployeePolicy findEmployeePolicyBy(int employeeId) {
        return employeePolicies.get(employeeId);
    }

}
