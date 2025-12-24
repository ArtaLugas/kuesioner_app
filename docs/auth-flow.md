# Auth & Session Flow

## Autentikasi
- Login berbasis email + password
- Session disimpan server-side
- Tidak ada JWT
- Tidak ada refresh token

## Invalidasi Session
- Password berubah
- Role berubah
- User dinonaktifkan
- Timeout idle / absolute

## Failure Response
Semua kegagalan auth/session → HTTP 403
Tanpa redirect, tanpa pesan bocor
