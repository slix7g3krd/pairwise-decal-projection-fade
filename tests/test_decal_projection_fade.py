import pytest
import graphics.decal_projection_fade as mod

CASES = [
    ("project_tangent_space", (1,)),
    ("decal_depth_test", (1,)),
    ("pool_visibility_evict", (1,)),
    ("grow_instance_buffer", (1,)),
    ("normal_follow_object", (1,)),
    ("sort_batch_by_material", (1,)),
    ("load", (1,)),
    ("project", (1,)),
    ("draw", (1,)),
    ("present", (1,)),
    ("validate_decal", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
