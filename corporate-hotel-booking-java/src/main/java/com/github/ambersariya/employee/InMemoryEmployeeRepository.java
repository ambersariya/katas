package com.github.ambersariya.employee;

import com.github.ambersariya.core.EmployeeId;

import java.util.HashMap;

public class InMemoryEmployeeRepository implements EmployeeRepository {
    private final HashMap<EmployeeId, Employee> employees = new HashMap<>();

    @Override
    public void addEmployee(Employee employee) {
        employees.put(employee.employeeId(), employee);
    }


    @Override
    public Employee findById(EmployeeId employeeId) {
        return employees.get(employeeId);
    }

    @Override
    public void deleteEmployee(EmployeeId employeeId) {
        employees.remove(employeeId);
    }

    public int size() {
        return employees.size();
    }
}
