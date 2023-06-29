package com.github.ambersariya.core;

import java.util.UUID;

public class UuidGenerator implements IdGenerator {

    @Override
    public String nextId() {
        return UUID.randomUUID().toString();
    }
}
