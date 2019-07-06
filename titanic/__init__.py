from titanic.controller import TitanicController
from titanic.view import TitanicView
if __name__ == '__main__':
    ctrl = TitanicController()
    t = ctrl.create_train()
    ctrl.test_all()
    # view = TitanicView()
    # t = view.create_train()
    # view.plot_pclass_sex(t)
    ctrl.submit()