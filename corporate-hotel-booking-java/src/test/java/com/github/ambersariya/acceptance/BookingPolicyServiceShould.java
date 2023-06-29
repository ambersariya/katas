package com.github.ambersariya.acceptance;

import com.github.ambersariya.booking.BookingPolicyService;
import com.github.ambersariya.booking.InMemoryBookingPolicyRepository;
import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.employee.Employee;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class BookingPolicyServiceShould {
    private static final CompanyId COMPANY_ID = new CompanyId("5c02072a-1a2e-4731-86e2-ef18859ddfb6");
    private static final int EMPLOYEE_ID = 1;
    private static final Employee EMPLOYEE = new Employee(EMPLOYEE_ID, COMPANY_ID);
    private InMemoryBookingPolicyRepository bookingPolicyRepository;
    private InMemoryEmployeeRepository employeeRepository;

    @BeforeEach
    public void setUp() {
        bookingPolicyRepository = new InMemoryBookingPolicyRepository();
        employeeRepository = new InMemoryEmployeeRepository();
        employeeRepository.addEmployee(EMPLOYEE);
    }

    @Test
    public void allow_booking_a_junior_suite_when_company_policy_doesnt_allow() {
        var companyRoomTypes = List.of(RoomType.STANDARD);
        var employeeRoomTypes = List.of(RoomType.JUNIOR_SUITE);

        var bookingPolicyService = new BookingPolicyService(bookingPolicyRepository, employeeRepository);
        bookingPolicyService.setCompanyPolicy(COMPANY_ID, companyRoomTypes);
        bookingPolicyService.setEmployeePolicy(EMPLOYEE_ID, employeeRoomTypes);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.JUNIOR_SUITE));
    }

    @Test
    public void allow_booking_a_standard_room_only_as_per_company_policy() {
        var companyRoomTypes = List.of(RoomType.STANDARD);

        var bookingPolicyService = new BookingPolicyService(bookingPolicyRepository, employeeRepository);
        bookingPolicyService.setCompanyPolicy(COMPANY_ID, companyRoomTypes);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD));
    }

    @Test
    public void allowed_to_book_any_room_when_neither_company_nor_employee_policies_exist() {
        var bookingPolicyService = new BookingPolicyService(bookingPolicyRepository, employeeRepository);

        assertTrue(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD));
    }
}
