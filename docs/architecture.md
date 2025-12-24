# Arsitektur Sistem

## Pola Arsitektur
Simplified Layered Monolith (Service-Centric)

## Lapisan
1. Routes (Blueprint per Role)
2. Middleware (Session, Role, Write Guard)
3. Policy Layer (Ownership + Status)
4. Service / Business Logic
5. Data Access (SQLAlchemy ORM)

## Prinsip
- Middleware tidak tahu business rule
- Policy tidak tahu HTTP
- Route tidak memutuskan izin sendiri
- Audit dicatat setelah aksi sah

## Alur Request (High Level)
Request →
Auth Session →
Session Guard →
Role Boundary →
Write Guard →
Policy →
Business Logic →
Audit →
Response
