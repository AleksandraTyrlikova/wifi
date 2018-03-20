## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    obj = bld.create_ns3_module('wifi', ['network', 'propagation', 'energy', 'spectrum', 'antenna', 'mobility'])
    obj.source = [
        'model/wifi-information-element.cc',
        'model/wifi-information-element-vector.cc',
        'model/wifi-channel.cc',
        'model/wifi-mode.cc',
        'model/ssid.cc',
        'model/wifi-phy.cc',
        'model/wifi-phy-state-helper.cc',
        'model/error-rate-model.cc',
        'model/yans-error-rate-model.cc',
        'model/nist-error-rate-model.cc',
        'model/dsss-error-rate-model.cc',
        'model/interference-helper.cc',
        'model/yans-wifi-phy.cc',
        'model/yans-wifi-channel.cc',
        'model/spectrum-wifi-phy.cc',
        'model/wifi-phy-tag.cc',
        'model/wifi-spectrum-phy-interface.cc',
        'model/wifi-spectrum-signal-parameters.cc',
        'model/wifi-mac-header.cc',
        'model/wifi-mac-trailer.cc',
        'model/mac-low.cc',
        'model/wifi-mac-queue.cc',
        'model/mac-tx-middle.cc',
        'model/mac-rx-middle.cc',
        'model/dca-txop.cc',
        'model/supported-rates.cc',
        'model/capability-information.cc',
        'model/status-code.cc',
        'model/mgt-headers.cc',
        'model/random-stream.cc',
        'model/dcf-manager.cc',
        'model/wifi-mac.cc',
        'model/regular-wifi-mac.cc',
        'model/wifi-remote-station-manager.cc',
        'model/ap-wifi-mac.cc',
        'model/sta-wifi-mac.cc',
        'model/adhoc-wifi-mac.cc',
        'model/wifi-net-device.cc',
        'model/arf-wifi-manager.cc',
        'model/aarf-wifi-manager.cc',
        'model/ideal-wifi-manager.cc',
        'model/constant-rate-wifi-manager.cc',
        'model/amrr-wifi-manager.cc',
        'model/onoe-wifi-manager.cc',
        'model/rraa-wifi-manager.cc',
        'model/aarfcd-wifi-manager.cc',
        'model/cara-wifi-manager.cc',
        'model/minstrel-wifi-manager.cc',
        'model/minstrel-ht-wifi-manager.cc',
        'model/qos-utils.cc',
        'model/edca-txop-n.cc',
        'model/msdu-aggregator.cc',
        'model/amsdu-subframe-header.cc',
        'model/msdu-standard-aggregator.cc',
        'model/originator-block-ack-agreement.cc',
        'model/dcf.cc',
        'model/ctrl-headers.cc',
        'model/qos-blocked-destinations.cc',
        'model/block-ack-agreement.cc',
        'model/block-ack-manager.cc',
        'model/block-ack-cache.cc',
        'model/snr-tag.cc',
        'model/ht-capabilities.cc',
        'model/wifi-tx-vector.cc',
        'model/parf-wifi-manager.cc',
        'model/aparf-wifi-manager.cc',
        'model/ampdu-subframe-header.cc',
        'model/mpdu-aggregator.cc',
        'model/mpdu-standard-aggregator.cc',
        'model/ampdu-tag.cc',
        'model/wifi-radio-energy-model.cc',
        'model/wifi-tx-current-model.cc',
        'model/vht-capabilities.cc',
        'model/erp-information.cc',
        'model/ht-operations.cc',
        'model/dsss-parameter-set.cc',
        'model/edca-parameter-set.cc',
        'helper/wifi-radio-energy-model-helper.cc',
        'helper/vht-wifi-mac-helper.cc',
        'helper/ht-wifi-mac-helper.cc',
        'helper/athstats-helper.cc',
        'helper/wifi-helper.cc',
        'helper/yans-wifi-helper.cc',
        'helper/spectrum-wifi-helper.cc',
        'helper/nqos-wifi-mac-helper.cc',
        'helper/qos-wifi-mac-helper.cc',
        'helper/wifi-mac-helper.cc',
        ]

    obj_test = bld.create_ns3_module_test_library('wifi')
    obj_test.source = [
        'test/block-ack-test-suite.cc',
        'test/dcf-manager-test.cc',
        'test/tx-duration-test.cc',
        'test/power-rate-adaptation-test.cc',
        'test/wifi-test.cc',
        'test/spectrum-wifi-phy-test.cc',
        'test/wifi-aggregation-test.cc',
        'test/wifi-error-rate-models-test.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'wifi'
    headers.source = [
        'model/wifi-information-element.h',
        'model/wifi-information-element-vector.h',
        'model/wifi-net-device.h',
        'model/wifi-channel.h',
        'model/wifi-mode.h',
        'model/ssid.h',
        'model/wifi-preamble.h',
        'model/wifi-phy-standard.h',
        'model/yans-wifi-phy.h',
        'model/spectrum-wifi-phy.h',
        'model/wifi-phy-tag.h',
        'model/yans-wifi-channel.h',
        'model/wifi-phy.h',
        'model/wifi-spectrum-phy-interface.h',
        'model/wifi-spectrum-signal-parameters.h',
        'model/interference-helper.h',
        'model/wifi-remote-station-manager.h',
        'model/ap-wifi-mac.h',
        'model/sta-wifi-mac.h',
        'model/adhoc-wifi-mac.h',
        'model/arf-wifi-manager.h',
        'model/aarf-wifi-manager.h',
        'model/ideal-wifi-manager.h',
        'model/constant-rate-wifi-manager.h',
        'model/amrr-wifi-manager.h',
        'model/onoe-wifi-manager.h',
        'model/rraa-wifi-manager.h',
        'model/aarfcd-wifi-manager.h',
        'model/cara-wifi-manager.h',
        'model/minstrel-wifi-manager.h',
        'model/minstrel-ht-wifi-manager.h',
        'model/wifi-mac.h',
        'model/regular-wifi-mac.h',
        'model/supported-rates.h',
        'model/error-rate-model.h',
        'model/yans-error-rate-model.h',
        'model/nist-error-rate-model.h',
        'model/dsss-error-rate-model.h',
        'model/wifi-mac-queue.h',
        'model/dca-txop.h',
        'model/wifi-mac-header.h',
        'model/wifi-mac-trailer.h',
        'model/wifi-phy-state-helper.h',
        'model/qos-utils.h',
        'model/edca-txop-n.h',
        'model/msdu-aggregator.h',
        'model/amsdu-subframe-header.h',
        'model/msdu-standard-aggregator.h',
        'model/mgt-headers.h',
        'model/status-code.h',
        'model/capability-information.h',
        'model/dcf-manager.h',
        'model/mac-tx-middle.h', 
        'model/mac-rx-middle.h', 
        'model/mac-low.h',
        'model/originator-block-ack-agreement.h',
        'model/dcf.h',
        'model/ctrl-headers.h',
        'model/block-ack-agreement.h',
        'model/block-ack-manager.h',
        'model/block-ack-cache.h',
        'model/snr-tag.h',
        'model/ht-capabilities.h',
        'model/parf-wifi-manager.h',
        'model/aparf-wifi-manager.h',
        'model/wifi-tx-vector.h',
        'model/ampdu-subframe-header.h',
        'model/mpdu-aggregator.h',
        'model/mpdu-standard-aggregator.h',
        'model/ampdu-tag.h',
        'model/wifi-radio-energy-model.h',
        'model/wifi-tx-current-model.h',
        'model/vht-capabilities.h',
        'model/erp-information.h',
        'model/ht-operations.h',
        'model/dsss-parameter-set.h',
        'model/edca-parameter-set.h',
        'helper/wifi-radio-energy-model-helper.h',
        'helper/vht-wifi-mac-helper.h',
        'helper/ht-wifi-mac-helper.h',
        'helper/athstats-helper.h',
        'helper/wifi-helper.h',
        'helper/yans-wifi-helper.h',
        'helper/spectrum-wifi-helper.h',
        'helper/nqos-wifi-mac-helper.h',
        'helper/qos-wifi-mac-helper.h',
        'helper/wifi-mac-helper.h',
        ]

    if bld.env['ENABLE_GSL']:
        obj.use.extend(['GSL', 'GSLCBLAS', 'M'])
        obj_test.use.extend(['GSL', 'GSLCBLAS', 'M'])

    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')

    bld.ns3_python_bindings()

