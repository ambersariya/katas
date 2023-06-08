package com.github.ambersariya.employee;

public interface EmployeeRepository {
    void addEmployee(Employee employee);

    Employee findById(int employeeId);

    void deleteEmployee(int employeeId);
}
