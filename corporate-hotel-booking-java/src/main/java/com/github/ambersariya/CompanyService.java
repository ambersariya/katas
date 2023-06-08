package com.github.ambersariya;

import com.github.ambersariya.employee.Employee;
import com.github.ambersariya.employee.EmployeeRepository;

public class CompanyService {

    private final EmployeeRepository employeeRepository;

    public CompanyService(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public void deleteEmployee(int employeeId) {
        employeeRepository.deleteEmployee(employeeId);
    }

    public void addEmployee(int employeeId, int companyId) {
        var employee = new Employee(employeeId, companyId);
        employeeRepository.addEmployee(employee);
    }
}
