# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023 Scipp contributors (https://github.com/scipp)
_version = '1'

__all__ = ['get_path']


def _make_pooch():
    import pooch

    return pooch.create(
        path=pooch.os_cache('ess/powgen'),
        env='ESS_DATA_DIR',
        base_url='https://public.esss.dk/groups/scipp/ess/dream/{version}/',
        version=_version,
        registry={
            'DREAM_nexus_sorted-2023-12-07.nxs': 'md5:22824e14f6eb950d24a720b2a0e2cb66',
        },
    )


_pooch = _make_pooch()


def get_path(name: str, unzip: bool = False) -> str:
    """
    Return the path to a data file bundled with ess.dream.

    This function only works with example data and cannot handle
    paths to custom files.
    """
    import pooch

    return _pooch.fetch(name, processor=pooch.Unzip() if unzip else None)
