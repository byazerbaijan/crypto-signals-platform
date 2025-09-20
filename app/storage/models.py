from sqlalchemy import Column, String, BigInteger, Float, Integer, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.storage.db import Base

class Symbol(Base):
    __tablename__ = "symbols"
    symbol: Mapped[str] = mapped_column(String(30), primary_key=True)
    base: Mapped[str] = mapped_column(String(20))
    quote: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20), default="TRADING")

class Kline(Base):
    """
    Универсальная таблица для разных интервалов.
    Уникальность: (symbol, interval, open_time)
    open_time/close_time — миллисекунды (Epoch ms) для простоты и скорости.
    """
    __tablename__ = "klines"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    symbol: Mapped[str] = mapped_column(String(30), index=True)
    interval: Mapped[str] = mapped_column(String(10), index=True)  # '1m','5m',...
    open_time: Mapped[int] = mapped_column(BigInteger)   # ms
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)
    close_time: Mapped[int] = mapped_column(BigInteger)  # ms
    quote_asset_volume: Mapped[float] = mapped_column(Float)
    number_of_trades: Mapped[int] = mapped_column(Integer)
    taker_buy_base_volume: Mapped[float] = mapped_column(Float)
    taker_buy_quote_volume: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        UniqueConstraint("symbol", "interval", "open_time", name="uq_kline"),
        Index("ix_klines_sym_intime", "symbol", "interval", "open_time"),
    )
