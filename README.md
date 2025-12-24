# Sistem WTP — Kuesioner & Wawancara

## Status Proyek
✅ Auth & Session Foundation — LOCKED  
✅ Role Group Routing — LOCKED  
✅ Write Guard (LOCKED status) — LOCKED  
✅ Policy (Ownership + Status) — LOCKED  
✅ Audit Log (Append-only) — LOCKED  

---

## Tujuan Sistem
Sistem ini digunakan untuk pendataan WTP berbasis wawancara dengan
alur terkontrol, audit-ready, dan tanpa privilege implisit.

---

## Arsitektur Teknis
- Backend: Flask (Service-Centric Monolith)
- ORM: SQLAlchemy
- Migration: Alembic
- Database: MySQL
- Auth: Session-based (server side)
- Tidak ada route publik

---

## Role
- SURV — Surveyor
- KOOR — Koordinator
- ADM — Admin

---

## Status Interview
DRAFT → SUBMITTED → VERIFIED → LOCKED

- LOCKED = read-only (system enforced)
- Tidak ada bypass, termasuk admin

---

## Prinsip Keamanan
- Session ≠ Permission
- Role ≠ Privilege global
- Status = kebenaran sistem
- Semua aksi penting tercatat di audit log

---

## Dokumentasi Teknis
Lihat folder `/docs`:
- `architecture.md`
- `auth-flow.md`
- `role-policy-matrix.md`
- `status-lifecycle.md`
- `audit-log.md`
- `decision-log.md`

---

## Catatan Freeze
Perubahan pada Auth, Role, Session, Policy, dan Audit
hanya boleh melalui:
- Perubahan matriks tertulis
- Keputusan arsitektur baru
