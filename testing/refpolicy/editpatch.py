with open("policy-rhel-7.3.z-contrib.patch.orig") as f:
    for line in f:
        if not line.startswith("diff --git "):
            if line.startswith("--- a/"):
                print "--- a/policy/modules/contrib/%s" % name
            elif line.startswith("+++ b/"):
                print "+++ b/policy/modules/contrib/%s" % name
            else:
                print line,
            continue
        name = line[len("diff --git a/"):]
        name = name[:name.rindex(" b/")]
        print "diff --git a/policy/modules/contrib/%s b/policy/modules/contrib/%s" % (name, name)
