class ClaripyError(Exception):
    pass

class UnsatError(ClaripyError):
    pass

class ClaripyFrontendError(ClaripyError):
    pass

class ClaripySerializationError(ClaripyError):
    pass

class BackendError(ClaripyError):
    pass

class ClaripyZ3Error(ClaripyError):
    pass

class ClaripyBackendVSAError(BackendError):
    pass

#
# AST errors
#

class ClaripyASTError(ClaripyError):
    pass

class ClaripyBalancerError(ClaripyASTError):
    pass

class ClaripyBalancerUnsatError(ClaripyBalancerError):
    pass

class ClaripyTypeError(ClaripyASTError):
    pass

class ClaripyValueError(ClaripyASTError):
    pass

class ClaripySizeError(ClaripyASTError):
    pass

class ClaripyOperationError(ClaripyASTError):
    pass

class ClaripyReplacementError(ClaripyASTError):
    pass

class ClaripyRecursionError(ClaripyOperationError):
    pass
