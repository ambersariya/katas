package com.github.ambersariya.unit.employee;

import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.employee.Employee;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

public class InMemoryEmployeeRepositoryShould {
    private static final int EMPLOYEE_ID = 1;
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");

    private static final Employee employee = new Employee(EMPLOYEE_ID, COMPANY_ID);
    private InMemoryEmployeeRepository employeeRepository;

    @BeforeEach
    public void setUp() {
        employeeRepository = new InMemoryEmployeeRepository();
    }

    @Test
    public void return_nothing_when_employee_does_not_exist() {
        assertNull(employeeRepository.findById(EMPLOYEE_ID));
    }

    @Test
    public void successfully_add_employee_when_they_dont_exist() {
        employeeRepository.addEmployee(employee);
        assertEquals(1, employeeRepository.size());
    }

    @Test
    public void not_add_employee_twice_when_one_exists_with_the_same_id() {
        employeeRepository.addEmployee(employee);
        employeeRepository.addEmployee(employee);
        assertEquals(1, employeeRepository.size());
    }

    @Test
    public void successfully_delete_existing_employee_by_id() {
        employeeRepository.addEmployee(employee);
        employeeRepository.deleteEmployee(EMPLOYEE_ID);
        assertNull(employeeRepository.findById(EMPLOYEE_ID));
    }
}
