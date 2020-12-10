void merge(const vector<int> &l, const vector<int> &r) {
    vector<int> v;
    int p1 = 0, p2 = 0;
    while (p1 < l.size() && p2 < r.size()) {
        if (l[p1] < r[p2]) {
            v.push_back(l[p1++]);
        } else {
            v.push_back(r[p2++]);
        }
    }
    while (p1 < l.size()) {
        v.push_back(l[p1++]);
    }
    while (p2 < r.size()) {
        v.push_back(r[p2++]);
    }
    return v;
}

void merge(const vector<int> &l, const vector<int> &r) {
    vector<int> v;
    int p1 = 0, p2 = 0;
    while (p1 < l.size() || p2 < r.size()) {
        if (p1 < l.size() && (p2 >= r.size() || l[p1] < r[p2])) {
            v.push_back(l[p1++]);
        } else {
            v.push_back(r[p2++]);
        }
    }
    return v;
}

void merge(const vector<int> &l, const vector<int> &r) {
    vector<int> v;
    auto get_elem = [](const vector<int> &v, int i) {
        return i >= v.size() ? inf : v[i];
    };
    int p1 = 0, p2 = 0;
    while (p1 < l.size() || p2 < r.size()) {
        if (get_elem(l, p1) < get_elem(r, p2)) {
            v.push_back(l[p1++]);
        } else {
            v.push_back(r[p2++]);
        }
    }
    return v;
}
