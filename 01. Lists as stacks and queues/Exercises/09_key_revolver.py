from collections import deque


def reloading_print(bullets, counter, gun_barrel_size):
    if bullets and counter % gun_barrel_size == 0:
        print('Reloading!')


def bang(locks, price, bullet_price, counter, gun_barrel_size, bullets):
    locks.popleft()
    price -= bullet_price
    print('Bang!')
    reloading_print(bullets, counter, gun_barrel_size)

    return price, bullets, locks


def ping(price, bullet_price, counter, gun_barrel_size, bullets):
    price -= bullet_price
    print('Ping!')
    reloading_print(bullets, counter, gun_barrel_size)

    return price


def key_revolver():
    bullet_price = int(input())
    gun_barrel_size = int(input())
    bullets = list(map(int, input().split(' ')))
    locks = deque(map(int, input().split(' ')))
    price = int(input())
    counter = 0

    while True:

        if locks:
            current_lock = locks[0]
        else:
            break

        if bullets:
            current_bullet = bullets.pop()
            counter += 1
        else:
            break

        if current_lock >= current_bullet:
            price, bullets, locks = bang(locks, price, bullet_price, counter, gun_barrel_size, bullets)
        else:
            price = ping(price, bullet_price, counter, gun_barrel_size, bullets)

    if len(locks) > 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        print(f"{len(bullets)} bullets left. Earned ${price}")


key_revolver()
