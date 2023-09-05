package com.github.ambersariya.acceptance;

import com.github.ambersariya.CompanyService;
import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertNull;

public class CompanyServiceShould {
    private static final EmployeeId EMPLOYEE_ID = new EmployeeId("a3a42ad5-8610-4d63-81a8-44915281332c");
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");
    private InMemoryEmployeeRepository employeeRepository;
    private CompanyService companyService;

    @BeforeEach
    public void setUp() {
        employeeRepository = new InMemoryEmployeeRepository();
        companyService = new CompanyService(employeeRepository);
    }

    @Test
    public void delete_an_employee_by_id() {
        companyService.addEmployee(EMPLOYEE_ID, COMPANY_ID);
        companyService.deleteEmployee(EMPLOYEE_ID);

        assertNull(employeeRepository.findById(EMPLOYEE_ID));
    }
}
