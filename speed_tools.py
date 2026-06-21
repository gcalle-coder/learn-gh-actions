"""Utilidades simples de velocidad/frenado, solo para practicar CI/CD."""


def kmh_to_ms(speed_kmh: float) -> float:
    """Convierte km/h a m/s."""
    return speed_kmh / 3.6


def ms_to_kmh(speed_ms: float) -> float:
    """Convierte m/s a km/h."""
    return speed_ms * 3.6


def braking_distance(speed_ms: float, deceleration: float) -> float:
    """Distancia de frenado (m) dada v inicial (m/s) y deceleración (m/s^2)."""
    if deceleration <= 0:
        raise ValueError("La deceleración debe ser positiva")
    return (speed_ms ** 2) / (2 * deceleration)
