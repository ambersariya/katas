package com.github.ambersariya.acceptance;

import com.github.ambersariya.CompanyService;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertNull;

public class CompanyServiceShould {
    private static final int EMPLOYEE_ID = 1;
    private static final int COMPANY_ID = 1;
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
