def dict_pack_unpack(*args, **kwargs):
    print("kwargs", kwargs)
    print("args", args)


dict_pack_unpack(4, 5, "goal", name="Shola", age=45, sex="Male")
