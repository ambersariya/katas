package com.github.ambersariya.booking;

import java.util.HashMap;

public class InMemoryBookingPolicyRepository implements BookingPolicyRepository {
    private final HashMap<Integer, CompanyPolicy> companyPolicies = new HashMap<>();
    private final HashMap<Integer, EmployeePolicy> employeePolicies = new HashMap<>();

    @Override
    public void saveCompanyPolicy(CompanyPolicy companyPolicy) {
        companyPolicies.put(companyPolicy.companyId(), companyPolicy);
    }

    @Override
    public void saveEmployeePolicy(EmployeePolicy employeePolicy) {
        employeePolicies.put(employeePolicy.employeeId(), employeePolicy);
    }

    @Override
    public CompanyPolicy findCompanyPolicyBy(int companyId) {
        if (!companyPolicies.containsKey(companyId)) {
            throw new CompanyBookingPolicyNotFound();
        }
        return companyPolicies.get(companyId);
    }

    @Override
    public EmployeePolicy findEmployeePolicyBy(int employeeId) {
        if (!employeePolicies.containsKey(employeeId)) {
            throw new EmployeeBookingPolicyNotFound();
        }
        return employeePolicies.get(employeeId);
    }

    @Override
    public int findCompanyIdBy(int employeeId) {
        throw new UnsupportedOperationException();
    }
}
