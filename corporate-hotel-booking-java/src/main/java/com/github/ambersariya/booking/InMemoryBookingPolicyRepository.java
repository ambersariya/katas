package com.github.ambersariya.booking;

public class InMemoryBookingPolicyRepository implements BookingPolicyRepository {
    @Override
    public void saveCompanyPolicy(CompanyPolicy companyPolicy) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void saveEmployeePolicy(EmployeePolicy employeePolicy) {
        throw new UnsupportedOperationException();
    }

    @Override
    public CompanyPolicy findCompanyPolicyBy(int companyId) {
        throw new UnsupportedOperationException();
    }

    @Override
    public EmployeePolicy findEmployeePolicyBy(int employeeId) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int findCompanyIdBy(int employeeId) {
        throw new UnsupportedOperationException();
    }
}
