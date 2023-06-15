package com.github.ambersariya.unit.booking;

import com.github.ambersariya.booking.CompanyPolicy;
import com.github.ambersariya.booking.EmployeeBookingPolicyNotFound;
import com.github.ambersariya.booking.EmployeePolicy;
import com.github.ambersariya.booking.InMemoryBookingPolicyRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class InMemoryBookingPolicyRepositoryShould {
    private static final int COMPANY_ID = 1;
    private static final int EMPLOYEE_ID = 1;
    private static final List<RoomType> COMPANY_ROOM_TYPES = List.of(RoomType.STANDARD);
    private static final List<RoomType> EMPLOYEE_ROOM_TYPES = List.of(RoomType.STANDARD, RoomType.JUNIOR_SUITE);
    private static final CompanyPolicy COMPANY_POLICY = new CompanyPolicy(COMPANY_ID, COMPANY_ROOM_TYPES);
    private static final EmployeePolicy EMPLOYEE_POLICY = new EmployeePolicy(COMPANY_ID, EMPLOYEE_ROOM_TYPES);
    private InMemoryBookingPolicyRepository bookingPolicyRepository;

    @BeforeEach
    public void setUp() {
        bookingPolicyRepository = new InMemoryBookingPolicyRepository();
    }

    @Test
    public void find_a_company_booking_policy_by_id() {
        bookingPolicyRepository.saveCompanyPolicy(COMPANY_POLICY);
        var result = bookingPolicyRepository.findCompanyPolicyBy(COMPANY_ID);

        assertEquals(COMPANY_POLICY, result);
    }

    @Test
    public void find_an_employee_policy_by_id() {
        bookingPolicyRepository.saveEmployeePolicy(EMPLOYEE_POLICY);
        var result = bookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID);

        assertEquals(EMPLOYEE_POLICY, result);
    }

    @Test
    public void throw_exception_when_company_policy_doesnt_exist() {
        assertThrows(EmployeeBookingPolicyNotFound.class, () -> bookingPolicyRepository.findEmployeePolicyBy(EMPLOYEE_ID));
    }
}
