package com.github.ambersariya.unit.employee;

import com.github.ambersariya.CompanyService;
import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.employee.Employee;
import com.github.ambersariya.employee.EmployeeRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.mockito.Mockito.verify;

@ExtendWith(MockitoExtension.class)
public class CompanyServiceShould {
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");
    private static final int EMPLOYEE_ID = 1;
    private static final Employee EMPLOYEE = new Employee(EMPLOYEE_ID, COMPANY_ID);
    @Mock
    private EmployeeRepository employeeRepository;

    @Test
    public void add_an_employee_by_id() {
        var companyService = new CompanyService(employeeRepository);
        companyService.addEmployee(EMPLOYEE_ID, COMPANY_ID);

        verify(employeeRepository).addEmployee(EMPLOYEE);
    }
}
