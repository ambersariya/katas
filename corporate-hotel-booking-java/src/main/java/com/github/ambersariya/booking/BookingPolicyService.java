package com.github.ambersariya.booking;

import com.github.ambersariya.employee.EmployeeRepository;
import com.github.ambersariya.hotel.RoomType;

import java.util.List;

public class BookingPolicyService {
    private final BookingPolicyRepository bookingPolicyRepository;
    private final EmployeeRepository employeeRepository;

    public BookingPolicyService(BookingPolicyRepository bookingPolicyRepository, EmployeeRepository employeeRepository) {
        this.bookingPolicyRepository = bookingPolicyRepository;
        this.employeeRepository = employeeRepository;
    }

    public void setCompanyPolicy(int companyId, List<RoomType> companyRoomTypes) {
        var companyPolicy = new CompanyPolicy(companyId, companyRoomTypes);
        bookingPolicyRepository.save(companyPolicy);
    }

    public void setEmployeePolicy(int employeeId, List<RoomType> employeeRoomTypes) {
        var employeePolicy = new EmployeePolicy(employeeId, employeeRoomTypes);
        bookingPolicyRepository.save(employeePolicy);
    }

    public boolean isBookingAllowed(int employeeId, RoomType roomType) {
        var employeePolicy = bookingPolicyRepository.findEmployeePolicyBy(employeeId);
        if (employeePolicy != null) {
            return employeePolicy.roomTypes().contains(roomType);
        }

        var employee = employeeRepository.findById(employeeId);
        var companyPolicy = bookingPolicyRepository.findCompanyPolicyBy(employee.companyId());
        if (companyPolicy != null) {
            return companyPolicy.roomTypes().contains(roomType);
        }

        return true;
    }
}
