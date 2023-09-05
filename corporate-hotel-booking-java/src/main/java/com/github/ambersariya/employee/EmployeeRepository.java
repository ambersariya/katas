package com.github.ambersariya.employee;

import com.github.ambersariya.core.EmployeeId;

public interface EmployeeRepository {
    void addEmployee(Employee employee);

    Employee findById(EmployeeId employeeId);

    void deleteEmployee(EmployeeId employeeId);
}
