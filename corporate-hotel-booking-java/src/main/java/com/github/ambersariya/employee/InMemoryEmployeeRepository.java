package com.github.ambersariya.employee;

import java.util.HashMap;

public class InMemoryEmployeeRepository implements EmployeeRepository {
    private final HashMap<Integer, Employee> employees = new HashMap<>();

    @Override
    public void addEmployee(Employee employee) {
        employees.put(employee.employeeId(), employee);
    }


    @Override
    public Employee findById(int employeeId) {
        return employees.get(employeeId);
    }

    @Override
    public void deleteEmployee(int employeeId) {
        employees.remove(employeeId);
    }

    public int size() {
        return employees.size();
    }
}
