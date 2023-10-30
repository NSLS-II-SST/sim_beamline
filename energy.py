import asyncio
from caproto.server import PVGroup, SubGroup, ioc_arg_parser, pvproperty, run, PvpropertyDouble
from caproto.ioc_examples.fake_motor_record import FakeMotor
from caproto import ChannelType


class MonoGrating(PVGroup):
    setpoint = pvproperty(name="_TYPE_SP", record="mbbo", value="1200l/mm",
                          enum_strings=["ZERO", "ONE", "250l/mm", "THREE", "FOUR",
                                        "FIVE", "SIX", "SEVEN", "EIGHT", "1200l/mm"],
                          dtype=ChannelType.ENUM)
    readback = pvproperty(name="_TYPE_MON", record="mbbo", value="1200l/mm",
                          enum_strings=["1200l/mm", "250l/mm"],
                          dtype=ChannelType.ENUM,
                          read_only=True)
    actuate = pvproperty(name="_DCPL_CALC.PROC")
    enable = pvproperty(name="_ENA_CMD.PROC")
    kill = pvproperty(name="_KILL_CMD.PROC")
    home = pvproperty(name="_HOME_CMD.PROC")
    clear = pvproperty(name="_ENC_LSS_CLR_CMD.PROC")
    done = pvproperty(name="_AXIS_STS")

    def __init__(self, delay=0.5, **kwargs):
        super().__init__(**kwargs)
        self._delay = delay

    @actuate.putter
    async def actuate(self, instance, value):
        await self.done.write(0)
        await asyncio.sleep(self._delay)
        sp = self.setpoint.value
        await self.readback.write(value=sp)
        await self.done.write(1)


class Mono(PVGroup):
    mono = SubGroup(FakeMotor, prefix="",  velocity=500, precision=3)
    gratingx = SubGroup(MonoGrating, prefix="GrtX}}Mtr")
    cff = pvproperty(name=":CFF_SP", value=1.55, dtype=PvpropertyDouble)


class Energy(PVGroup):
    mono =  SubGroup(Mono, prefix="MonoMtr")
    gap =   SubGroup(FakeMotor, prefix="GapMtr",   velocity=5000, precision=3)
    phase = SubGroup(FakeMotor, prefix="PhaseMtr", velocity=5000, precision=3)
    mode =  SubGroup(FakeMotor, prefix="ModeMtr",  velocity=100, precision=3)
