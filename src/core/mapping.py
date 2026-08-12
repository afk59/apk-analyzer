
import sys
import json
from pathlib import Path


KIT_DOC_URLS: dict[str, str] = {
    "@kit.AbilityKit":            "https://developer.huawei.com/consumer/en/doc/harmonyos-guides/abilitykit-overview",
    "@kit.AccessibilityKit":      "https://developer.huawei.com/consumer/en/doc/harmonyos-guides/accessibility-kit",
    "@kit.AccountKit":            "https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-kit-guide",
    "@kit.AdsKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ads-kit-guide-V5",
    "@kit.AppGalleryKit":         "https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-arkts",
    "@kit.ArkData":               "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/arkdata-V5",
    "@kit.ArkGraphics2D":         "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/arkgraphics-2d-V5",
    "@kit.ArkGraphics3D":         "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/arkgraphics-3d-V5",
    "@kit.ArkUI":                 "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/arkui-V5",
    "@kit.ArkWeb":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/arkweb-V5",
    "@kit.AREngine":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ar-engine-kit-guide-V5",
    "@kit.AudioKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/audio-kit-V5",
    "@kit.BackgroundTasksKit":    "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/background-task-kit-V5",
    "@kit.BasicServicesKit":      "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/basic-services-kit-V5",
    "@kit.CalendarKit":           "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/calendar-kit-V5",
    "@kit.CameraKit":             "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/camera-kit-V5",
    "@kit.CloudFoundationKit":    "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/cloud-foundation-kit-guide-V5",
    "@kit.ConnectivityKit":       "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/connectivity-kit-V5",
    "@kit.ContactsKit":           "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/contacts-kit-V5",
    "@kit.CoreFileKit":           "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/core-file-kit-V5",
    "@kit.CoreSpeechKit":         "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/core-speech-kit-guide-V5",
    "@kit.CoreVisionKit":         "https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-vision-objectdetection",
    "@kit.CryptoArchitectureKit": "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/core-speech-kit-guide-V5",
    "@kit.DeviceCertificateKit":  "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/device-certificate-kit-V5",
    "@kit.DriverDevelopmentKit":  "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/driver-development-kit-V5",
    "@kit.DrmKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/drm-kit-V5",
    "@kit.GameServiceKit":        "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/game-service-kit-guide-V5",
    "@kit.HealthServiceKit":      "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/health-service-kit-guide-V5",
    "@kit.IAPKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/iap-kit-guide-V5",
    "@kit.IMEKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ime-kit-V5",
    "@kit.ImageKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/image-kit-V5",
    "@kit.InputKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/input-kit-V5",
    "@kit.IPCKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ipc-kit-V5",
    "@kit.LocationKit":           "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/location-kit-V5",
    "@kit.MapKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/map-kit-guide-V5",
    "@kit.MediaKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/media-kit-V5",
    "@kit.MindSporeLiteKit":       "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/mindspore-lite-kit-V5",
    "@kit.NaturalLanguageKit":     "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/natural-language-kit-V5",
    "@kit.NetworkKit":             "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/network-kit-V5",
    "@kit.NotificationKit":        "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/notification-kit-V5",
    "@kit.PerformanceAnalysisKit": "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/performance-analysis-kit-V5",
    "@kit.PushKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/push-kit-guide-V5",
    "@kit.ScanKit":                "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/scan-kit-guide-V5",
    "@kit.SensorServiceKit":       "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/sensor-service-kit-V5",
    "@kit.ServiceCollaborationKit":"https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/service-collaboration-kit-guide-V5",
    "@kit.SpeechKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/speech-kit-guide-V5",
    "@kit.TelephonyKit":           "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/telephony-kit-V5",
    "@kit.UniversalKeystoreKit":   "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/huks-kit-V5",
    "@kit.UserAuthenticationKit":  "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/user-authentication-kit-V5",
    "@kit.VisionKit":              "https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/user-authentication-kit-V5"
}

HMS_DOC_URLS: dict[str, str] = {
    "Account Kit":            "https://developer.huawei.com/consumer/en/hms/huawei-accountkit/",
    "Ads Kit":                "https://developer.huawei.com/consumer/en/hms/huawei-adskit/",
    "Analytics Kit":          "https://developer.huawei.com/consumer/en/hms/huawei-analyticskit/",
    "App Linking":            "https://developer.huawei.com/consumer/en/agconnect/App-linking/",
    "AR Engine":              "https://developer.huawei.com/consumer/en/hms/huawei-arengine/",
    "Audio Kit":              "https://developer.huawei.com/consumer/en/hms/huawei-audiokit/",
    "Audio Editor Kit":       "https://developer.huawei.com/consumer/en/hms/huawei-audio-editor/",
    "AV Pipeline Kit":        "https://developer.huawei.com/consumer/en/hms/huawei-av-pipeline/",
    "Awareness Kit":          "https://developer.huawei.com/consumer/en/hms/huawei-awarenesskit/",
    "Camera Engine":          "https://developer.huawei.com/consumer/en/CameraKit/",
    "Cast Engine":            "https://developer.huawei.com/consumer/en/cast-kit",
    "Computer Graphics Kit":  "https://developer.huawei.com/consumer/en/hms/huawei-computer-graphics/",
    "Drive Kit":              "https://developer.huawei.com/consumer/en/hms/huawei-drivekit/",
    "FIDO":                   "https://developer.huawei.com/consumer/en/hms/huawei-fido/",
    "Game Service":           "https://developer.huawei.com/consumer/en/hms/huawei-game",
    "Health Kit":             "https://developer.huawei.com/consumer/en/hms/huaweihealth/",
    "HUAWEI HiAI Engine":     "https://developer.huawei.com/consumer/en/hiai#Engine",
    "HUAWEI HiAI Service":    "https://developer.huawei.com/consumer/en/hiai#Service",
    "Image Kit":              "https://developer.huawei.com/consumer/en/hms/huawei-imagekit/",
    "In-App Purchases":       "https://developer.huawei.com/consumer/en/hms/huawei-iap/",
    "Location Kit":           "https://developer.huawei.com/consumer/en/hms/huawei-locationkit/",
    "Map Kit":                "https://developer.huawei.com/consumer/en/hms/huawei-MapKit",
    "ML Kit":                 "https://developer.huawei.com/consumer/en/hms/huawei-mlkit/",
    "Nearby Service":         "https://developer.huawei.com/consumer/en/hms/huawei-nearbyservice/",
    "Network Kit":            "https://developer.huawei.com/consumer/en/hms/huawei-networkkit/",
    "Push Kit":               "https://developer.huawei.com/consumer/en/hms/huawei-pushkit/",
    "Safety Detect":          "https://developer.huawei.com/consumer/en/hms/huawei-safetydetectkit/",
    "Scan Kit":               "https://developer.huawei.com/consumer/en/hms/huawei-scankit/",
    "Scene Kit":              "https://developer.huawei.com/consumer/en/hms/huawei-scenekit/",
    "Search Kit":             "https://developer.huawei.com/consumer/en/hms/huawei-searchkit/",
    "Site Kit":               "https://developer.huawei.com/consumer/en/hms/huawei-sitekit/",
    "Video Kit":              "https://developer.huawei.com/consumer/en/hms/huawei-videokit/",
    "Video Editor Kit":       "https://developer.huawei.com/consumer/en/hms/huawei-video-editor/",
    "Wallet Kit":             "https://developer.huawei.com/consumer/en/hms/huawei-walletkit/",
    "Wear Engine":            "https://developer.huawei.com/consumer/en/hms/huawei-wearengine/",
    "Wireless Kit":           "https://developer.huawei.com/consumer/en/hms/huawei-wirelesskit/",
    "WisePlay DRM":           "https://developer.huawei.com/consumer/en/hms/huawei-wiseplay",
    "Keyring":                "https://developer.huawei.com/consumer/en/hms/huawei-keyring/",
    "Dynamic Tag Manager":     "https://developer.huawei.com/consumer/en/hms/huawei-dynamic-tag-manager/",
    "LocalAuthentication Engine": "https://developer.huawei.com/consumer/en/hms/huawei-localauthentication-engine/",
}


def load_mapping(mapping_path: Path) -> dict:
    from ui.terminal import print_warn
    if not mapping_path.exists():
        print_warn(f"Mapping file not found: {mapping_path}")
        sys.exit(1)
    with open(mapping_path, encoding="utf-8") as f:
        return json.load(f)


def load_ohpm_mapping(mapping_path: Path) -> dict | None:
    """Load the OHPM second-tier mapping. Returns None if unavailable.

    Deliberately does NOT `sys.exit(1)` the way `load_mapping` does. The native
    mapping is required — without it there is no analysis — but OHPM is an
    optional second tier layered on top of it. A missing or corrupt
    `ohpm_mapping.json` must degrade to "no OHPM tier", leaving every native
    result byte-identical, rather than killing the run. Same containment rule as
    `_ensure_play_scraper` vs `_ensure_deps`.
    """
    from ui.terminal import print_warn
    if not mapping_path.exists():
        return None
    try:
        with open(mapping_path, encoding="utf-8") as f:
            doc = json.load(f)
    except (OSError, ValueError) as exc:
        print_warn(f"OHPM mapping unreadable, second tier disabled — {exc}")
        return None
    if not isinstance(doc.get("ohpm_mappings"), list):
        print_warn("OHPM mapping has no 'ohpm_mappings' list — second tier disabled")
        return None
    return doc


def build_ohpm_entries(ohpm_doc: dict | None) -> list:
    """Sort OHPM rows longest-prefix-first, mirroring the native matcher.

    `apk_engine` sorts `namespace_mappings` by descending `android_namespace`
    length and breaks on the first prefix hit; the second tier uses the exact
    same shape so a longer OHPM prefix always beats a shorter one. Returns [] if
    there is no usable mapping, which disables the tier at zero cost.
    """
    if not ohpm_doc:
        return []
    rows = [r for r in ohpm_doc.get("ohpm_mappings", [])
            if isinstance(r, dict) and r.get("android_namespace") and r.get("ohpm_package")]
    return sorted(rows, key=lambda r: len(r["android_namespace"]), reverse=True)


def get_doc_url(kit_name: str, target: str = "hmos") -> str | None:
    if target == "hms":
        return HMS_DOC_URLS.get(kit_name)
    return KIT_DOC_URLS.get(kit_name)
